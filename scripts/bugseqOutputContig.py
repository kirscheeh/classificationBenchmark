#!/usr/bin/env python

# translating bugseq output into areport
import sys
import getting
from ete3 import NCBITaxa

def get_taxid(species):
    return list(NCBITaxa().get_name_translator([species]).values())[0][0] #get only taxid...

def get_rank(taxid):
    rank = list(NCBITaxa().get_rank([taxid]).values())[0][0]
    rankCode = {'v':'V','g':'G', 's':'ST', 'strain':'ST', 'subspecies':'SS', 'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', '2':'C', 'phylum':'P', 'kingdom': 'K'}
    try:
        return rankCode[str(rank)]
    except KeyError:
        #print(rank, taxid)
        return rank, taxid, '-' #everything else
    

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python bugseqOutput.py contig_classification.tsv new_file.areport")
else:
    if "366" in sys.argv[1]: # needs modification for other names
        sample="gridion366"
    else:
        sample="gridion364"

    #numContigs= getting.get_numberReadsSample(sample)
    with open(sys.argv[1], "r") as report:
        lines = report.readlines()
        numContigs=len(lines)
        print(numContigs)
        #numContigsUnclassified=int(lines[-1].split(",")[3])???
        #abundanceUnclassified=numContigsUnclassified/numContigs

        identified={}
        for line in lines[4:]:
            contig_name = line.split("\t")[0]
            scientific= line.split("\t")[1].split("; ")[-1][:-2]
            try:
                identified[scientific][1] += 1 #number hits
                identified[scientific][0] = identified[scientific][1]/numContigs
            except KeyError:
                taxid=get_taxid(scientific)
                rank=get_rank(taxid)
                identified[scientific]=[1/numContigs, 1, rank, taxid, scientific]

    areport = open(sys.argv[2], "w")
    areport.write("Abundance\tnumContigs\ttaxRank\ttaxID\tName\n")
        #areport.write(str(abundanceUnclassified)+"\t"+str(numContigsUnclassified)+"\t"+"U\t0\tunclassified")
    for species in identified.keys():
        entry_list=identified[species]
        areport.write("\n"+str(entry_list[0])+"\t"+str(entry_list[1])+"\t"+str(entry_list[2])+"\t"+str(entry_list[3])+"\t"+str(entry_list[4])) 
