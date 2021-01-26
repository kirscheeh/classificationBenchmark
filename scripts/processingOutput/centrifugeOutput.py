import sys

def get_rank(name):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    return rank_code[name]

if not len(sys.argv) == 4:
    print("An error occured.")
    print("Usage: python centrifugeOutput.py PATH/TO/file.CLASSIFICATION PATH/TOfile.REPORT PATH/TO/NEW_FILE.areport")
else:
    unclassified=0
    with open (sys.argv[1], 'r') as classify:
        lines=classify.readlines()
        num_reads = len(lines)-1 #due to header
        for line in lines[1:]:
            if line.split("\t")[1] == "unclassified":
                    unclassified +=1

    abundance_unclassified=unclassified/num_reads

    new_file = open(sys.argv[3], "a")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName")
    new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")

    with open(sys.argv[2], "r") as report:
        species = report.readlines()

        for line in species[1:]:
            l = line.split("\t")
            hits = int(l[4])
            abundance = hits/num_reads
            rank = get_rank(l[2])
            taxID = l[1]
            species_name=l[0]
            new_file.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name))