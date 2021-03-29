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
    print("Usage: python diamondOutput.py PATH/TO/file.CLASSIFICATION PATH/TO/NEW_FILE.areport")
else:
    unclassified=0
#    with open (sys.argv[1], 'r') as classify:
 #       lines=classify.readlines()
  #      num_reads = len(lines)
       # for line in lines[1:]:
        #    if line.split("\t")[1] == "0":
         #           unclassified +=1 
        
    #abundance_unclassified=0#unclassified/num_reads

    print("Starting...")
    
    with open(sys.argv[1], "r") as report:
        species = report.readlines()
        num_reads=len(species)   
        matches={}
        hits=0
        line_counter=0
        counting=0
        for line in species:
            l = line.split("\t")
            if l[1] == "0":
                unclassified+=1
            else:
                taxID = l[1]
                try:
                    hits=matches[taxID][1]+1
                except KeyError:
                    hits=1
                abundance = hits/num_reads
                rank = get_rank(l[1])
                species_name=list(taxId2Species(l[1]).values())[0]
                matches[taxID]=(abundance, hits, rank, taxID, species_name)
            line_counter+=1
            if line_counter == 10000:
                counting+=1
                print(str(counting)+"/"+str(round(num_reads/10000)))
                line_counter=0
    
    abundance_unclassified=unclassified/num_reads
    
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")
    
    for elem in matches.values():
        new_file.write("\n"+str(elem[0])+"\t"+str(elem[1])+"\t"+str(elem[2])+"\t"+str(elem[3])+"\t"+str(elem[4]))

    
    """new_file.close()
    with open(sys.argv[2], 'r') as f:
        lines=f.readlines()
        lines[1]=str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified\n"

    with open(sys.argv[2], 'w') as f:
        for line in lines:
            f.write(line)"""
