import sys
from ete3 import NCBITaxa
import getting

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
    sample=getting.get_sampleName(sys.argv[1])

    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(0)+"\t"+str(0)+"\t"+"U\t0\tunclassified\n")
    
    classifiedEntry={}
    classified=0
    with open(sys.argv[1], 'r') as report:
        lines=report.readlines()
        for line in lines[1:]:
            try:
                taxid=int(line.split("|")[0].split("\"")[-1])
            except ValueError:
                pass
            
            species = taxId2Species(taxid)[taxid]
            rank = get_rank(taxid)
            
            try: #depending on name of refseq
                l = line.split("\",")[1].split(",")[0]
            except Exception:
                l = line.split(",")[1]
            
            current_numReads=int(l)
            classified+=current_numReads
            
            try: # check if there is another entry with that taxid
                old_numReads = classifiedEntry[taxid][1]
            except KeyError:
                old_numReads=0
            
            classifiedEntry[taxid]=(0, current_numReads+old_numReads, rank, taxid, species)
    
    sampleSize = getting.get_numberReadsSample(sample)
    unclassified=sampleSize-classified
    
    for key in classifiedEntry.values():
        abundance = key[1]/sampleSize
        new_file.write(str(abundance)+"\t"+str(key[1])+"\t"+str(key[2])+"\t"+str(key[3])+"\t"+str(key[4])+"\n")
    new_file.close()
    
    abundance_unclassified=unclassified/classified
    with open(sys.argv[2], 'r') as f:
        lines=f.readlines()
        lines[1]=str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified\n"

    with open(sys.argv[2], 'w') as f:
        for line in lines:
            f.write(line)


