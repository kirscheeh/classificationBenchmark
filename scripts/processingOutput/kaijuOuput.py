import sys
from os import walk

def get_rank(filename):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    return rank_code[filename.split(".")[-2]]

if not len(sys.argv) == 4:
    print("An error occured.")
    print("Usage: python kaijuOutput.py PATH/TO/FILE.CLASSIFICATION PATH/TO/REPORTS.REPORT PATH/TO/NEW_FILE.areport")
else:
    unclassified=0
    with open (sys.argv[1], 'r') as classification:
        lines=classification.readlines()
        num_reads = len(lines)
        for line in lines:
            if line.split("\t")[0] == "U":
                    unclassified +=1
    abundance_unclassified=unclassified/num_reads
    new_file = open(sys.argv[3], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")

    prefix = sys.argv[2].split("/")[-1]
    
    # since I only consider species level

    #path = sys.argv[2][:-len(prefix)]
    #_, _, filenames = next(walk(path))
    #for filename in filenames:
        #if prefix in filename and filename.split(".")[-1]=="report":
    
    with open(sys.argv[2], "r") as report:#str(path)+str(prefix)
        species = report.readlines()

        for line in species[1:]:
            l = line.split("\t")
            hits = int(l[2])
            abundance = hits/num_reads
            #rank = get_rank(filename)
            taxID = l[3]
            species_name=l[4][:-1]
            new_file.write("\n"+str(abundance)+"\t"+str(hits)+"\tS"+"\t"+str(taxID)+"\t"+str(species_name))#+str(rank)
