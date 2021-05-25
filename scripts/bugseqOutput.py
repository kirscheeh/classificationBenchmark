#!/usr/bin/env python

# translating bugseq output into areport
import sys
import getting

def get_rank(tax):
    rankCode = {'strain':'ST', 'subspecies':'SS', 'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', '2':'C', 'phylum':'P', 'kingdom': 'K'}
    try:
        return rankCode[str(tax)]
    except KeyError:
        return '-' #everything else

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python bugseqOutput.py classification.tsv new_file.areport")
else:
    if "366" in sys.argv[1]: # needs modification for other names
        sample="gridion366"
    else:
        sample="gridion364"

    numReads= getting.get_numberReadsSample(sample)
    with open(sys.argv[1], "r") as report:
        lines = report.readlines()
        #numReadsUnclassified=int(lines[-1].split(",")[3])???
        #abundanceUnclassified=numReadsUnclassified/numReads

        areport = open(sys.argv[2], "w")
        areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
        #areport.write(str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified")

        for line in lines[4:]:
            l = line.split("\t")
            hits = int(l[1])
            abundance = hits/numReads
            rank = get_rank(str(l[4]))
            taxID = l[0]
            species_name=l[5].split("\n")[:-1][0]
            areport.write("\n"+str(0)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name)) #abundance

