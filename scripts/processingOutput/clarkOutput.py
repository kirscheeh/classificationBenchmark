import sys

def get_rank(lineage):
    tax = lineage.split(";")
    rank_code = {'6': 'S', '5': 'G', '4': 'F', '3':'O', '2':'C', '1':'P', '1': 'K'}#, '0': 'D'}
    return rank_code[str(len(tax))]

if not len(sys.argv) == 4:
    print("An error occured.")
    print("Usage: python centrifugeOutput.py PATH/TO/file.CLASSIFICATION PATH/TO/FILE.report PATH/TO/NEW_FILE.areport")
else:
    unclassified=0
    """with open (sys.argv[1], 'r') as classify:
        lines=classify.readlines()
        num_reads = len(lines)-1 #due to header
        """
    
    num_reads=3491391
    with open(sys.argv[2], "r") as report:
        species = report.readlines()
        unclassified=int(species[-1].split(",")[3])
        abundance_unclassified=unclassified/num_reads

        new_file = open(sys.argv[3], "w")
        new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
        new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")

        for line in species[1:-1]:
            l = line.split(",")
            hits = int(l[3])
            abundance = hits/num_reads
            rank = get_rank(l[2])
            taxID = l[1]
            species_name=l[0]
            new_file.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name))

