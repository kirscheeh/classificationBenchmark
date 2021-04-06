#!/usr/bin/env python
# translating kslam output into areport
import sys
from ete3 import NCBITaxa
import getting

def get_rank(taxid): # get rank until species level
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    try:
        return rank_code[NCBITaxa().get_rank([int(taxid)])[int(taxid)]]
    except KeyError: #species group, strain, clade
       return "-"

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python kslamOutput.py file.classification new_file.areport")
else:
    areport = open(sys.argv[2], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    areport.write(str(0)+"\t"+str(0)+"\t"+"U\t0\tunclassified\n") #space holder

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        i=0
        numReadsClassified=0
        abundanceClassified=0
        
        for line in lines:
            if "<taxon>" in line:
                numReadsTaxon = lines[i+1].split("\"")[1]
                abundanceTaxon=float(lines[i+1].split("\"")[2].split("<")[0][1:])/100
                taxid=lines[i+2].split(">")[1].split("<")[0]
                name=lines[i+4].split("name")[1][1:-2]
                rank=get_rank(int(taxid))
                
                areport.write(str(abundanceTaxon)+"\t"+numReadsTaxon+"\t"+rank+"\t"+"\t"+name+"\n")
                
                numReadsClassified+=int(numReadsTaxon)
                abundanceClassified+=float(abundanceTaxon)
            i+=1

        numReadsTotal=numReadsClassified/abundanceClassified
        numReadsUnclassified=numReadsTotal-numReadsClassified
        abundanceUnclassified=1-abundanceClassified

    areport.close()
    print(numReadsTotal)
    sample=getting.get_sampleName(sys.argv[1])
    sampleSize =getting.get_numberReadsSample(sample)
    print(sampleSize)
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()
        # write stats for unclassified into file
        lines[1]=str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified\n"
    
    with open(sys.argv[2], 'w') as f:
        for line in lines:
            f.write(line)
