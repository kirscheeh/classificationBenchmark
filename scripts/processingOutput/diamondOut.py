import sys
from ete3 import NCBITaxa

def taxId2Species(taxid):
    return NCBITaxa().get_taxid_translator([taxid])

def get_rank(taxid):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    return rank_code[NCBITaxa().get_rank([int(taxid)])[int(taxid)]]

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python centrifugeOutput.py PATH/TO/file.CLASSIFICATION PATH/TO/NEW_FILE.areport")
else:
    unclassified=0
    with open (sys.argv[1], 'r') as classify:
        lines=classify.readlines()
        num_reads = len(lines)
        for line in lines[1:]:
            if line.split("\t")[1] == "0":
                    unclassified +=1 
        
    abundance_unclassified=unclassified/num_reads
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")
    
    with open(sys.argv[1], "r") as report:
        species = report.readlines()
        matches={}
        hits=0
        for line in species:
            l = line.split("\t")
            if not l[1] == "0":
                taxID = l[1]
                try:
                    print(line)
                    hits=matches[taxID][1]+1
                except KeyError:
                    hits=1
                print(taxID, hits, num_reads)
                abundance = hits/num_reads
                rank = get_rank(l[1])
                species_name=list(taxId2Species(l[1]).values())[0]
                matches[taxID]=(abundance, hits, rank, taxID, species_name)
    
    for elem in matches.values():
        new_file.write("\n"+str(elem[0])+"\t"+str(elem[1])+"\t"+str(elem[2])+"\t"+str(elem[3])+"\t"+str(elem[4]))