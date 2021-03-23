import sys
from ete3 import NCBITaxa

def taxId2Species(taxid):
    return NCBITaxa().get_taxid_translator([taxid])

def get_rank(taxid):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    try:
        return rank_code[NCBITaxa().get_rank([int(taxid)])[int(taxid)]]
    except KeyError: #species group, strain, clade
       return "-"

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python ccmetagenOutput.py FILE.REPORT NEW_FILE.areport")
else:
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(0)+"\t"+str(0)+"\t"+"U\t0\tunclassified\n")
    classified={}
    total_num=0
    unclassified=0
    with open(sys.argv[1], 'r') as report:
        lines=report.readlines()
        for line in lines[1:]:
            try:
                taxid=int(line.split("|")[0].split("\"")[-1])
            except ValueError:
                pass#unclassified+=int(line.split(",")[1])
            species = taxId2Species(taxid)[taxid]
            rank = get_rank(taxid)
            try:
                l = line.split("\",")[1].split(",")[0]
            except Exception:
                l = line.split(",")[1]
            numreads=int(l)
            if not taxid:
                unclassified+=l
            total_num+=numreads
            try:
                current_numreads = classified[taxid][1]
            except KeyError:
                current_numreads=0
            classified[taxid]=(0, numreads+current_numreads, rank, taxid, species)
    
    new_file.write(str(total_num)+"\t"+str(unclassified)+"\n")
    for key in classified.values():
        new_file.write(str(0)+"\t"+str(key[1])+"\t"+str(key[2])+"\t"+str(key[3])+"\t"+str(key[4])+"\n")


