import sys
from os import walk

def get_rank(filename):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    return rank_code[filename.split(".")[-2]]

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python kaijuOutput.py PATH/TO/REPORTS.REPORT PATH/TO/NEW_FILE.areport")
else:
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(0)+"\t"+str(0)+"\t"+"U\t0\tunclassified")

    prefix = sys.argv[1].split("/")[-1]
    total_number=0
    with open(sys.argv[1], "r") as report:
        species = report.readlines()

        for line in species[1:]:
            l = line.split("\t")

            if l[4][:-1]=="unclassified":
                num_reads=int(l[2])
                abundance_unclassified=float(l[1])/100
                total_number+=num_reads
            else:
                hits = int(l[2])
                total_number+=hits

                taxID = l[3]
                species_name=l[4][:-1]
                abundance=float(l[1])/100
                new_file.write("\n"+str(abundance)+"\t"+str(hits)+"\tS"+"\t"+str(taxID)+"\t"+str(species_name))
    new_file.close()
    
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()
        lines[1]= "\n"+str(abundance_unclassified)+"\t"+str(num_reads)+"\tU"+"\t"+str(0)+"\tunclassified\n"#+str(rank)
    
    for line in lines[1:]:
        line=line.split("\t")
        print(int(line[1])/num_reads)
    with open(sys.argv[2], 'w') as f:
        f.write("Abundance\tnumReads\ttaxRank\ttaxID\tName")
        for line in lines[1:]:
            f.write(line)
