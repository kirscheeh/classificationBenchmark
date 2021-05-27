# translating kaiju output into areport
import sys

def get_rank(filename):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    return rank_code[filename.split(".")[-2]] 

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python kaijuOutput.py file.report new_file.areport")
else:
    areport = open(sys.argv[2], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    areport.write(str(0)+"\t"+str(0)+"\t"+"U\t0\tunclassified")

    with open(sys.argv[1], "r") as report:
        species = report.readlines()

        for line in species[1:]:
            l = line.split("\t")

            if l[4][:-1]=="unclassified":
                numReadsEntry=int(l[2])
                abundance_unclassified=float(l[1])/100
            else:
                hits = int(l[2])
                taxID = l[3]
                species_name=l[4][:-1]
                abundance=float(l[1])/100 # Kaiju has entry, but in %

                areport.write("\n"+str(abundance)+"\t"+str(hits)+"\tS"+"\t"+str(taxID)+"\t"+str(species_name)) #rank is always S, just species in report
    areport.close()
    
    # add first line
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()
        lines[1]= "\n"+str(abundance_unclassified)+"\t"+str(numReadsEntry)+"\tU"+"\t"+str(0)+"\tunclassified\n"
    
    with open(sys.argv[2], 'w') as f:
        f.write("Abundance\tnumReads\ttaxRank\ttaxID\tName")
        for line in lines[1:]:
            f.write(line)