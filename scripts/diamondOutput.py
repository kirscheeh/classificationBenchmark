
#!/usr/bin/env python
# translating diamond output into areport

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
    print("Usage: python diamondOutput.py file.CLASSIFICATION new_file.areport")
else:
    unclassified=0
    
    print("Starting...")
    
    with open(sys.argv[1], "r") as report:
        lines = report.readlines()
        numReadsTotal=len(lines)   
        
        # dic with information for each taxa
        matches={}
        
        # number of reads for given taxon
        hits=0
        
        # to give uopdate for many reads
        lineCounter=0 
        countingSteps=0
        
        for line in lines:
            l = line.split("\t")
            if l[1] == "0":
                unclassified+=1
            else:
                taxID = l[1]
                
                try: # basically check if already entry
                    hits=matches[taxID][1]+1
                except KeyError:
                    hits=1
                
                abundance = hits/numReadsTotal
                rank = get_rank(l[1])
                species_name=list(taxId2Species(l[1]).values())[0]
                matches[taxID]=(abundance, hits, rank, taxID, species_name)
            
            lineCounter+=1
            if lineCounter == 10000:
                countingSteps+=1
                print(str(countingSteps)+"/"+str(round(numReadsTotal/10000)))
                lineCounter=0
    
    abundance_unclassified=unclassified/numReadsTotal
    
    areport = open(sys.argv[2], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    areport.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")
    
    for elem in matches.values():
        areport.write("\n"+str(elem[0])+"\t"+str(elem[1])+"\t"+str(elem[2])+"\t"+str(elem[3])+"\t"+str(elem[4]))
