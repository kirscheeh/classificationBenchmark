#!/usr/bin/env python
# translating clark output into areport
import sys
import getting

def get_rank(lineage):
    tax = lineage.split(";")
    rankCode = {'6': 'S', '5': 'G', '4': 'F', '3':'O', '2':'C', '1':'P', '1': 'K'}#, '0': 'D'}
    return rankCode[str(len(tax))]

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python clarkOutput.py file.report new_file.areport")
else:
    sample = getting.get_sampleName(sys.argv[1])
    numReads= getting.get_numberReadsSample(sample)
    
    with open(sys.argv[2], "r") as report:
        lines = report.readlines()
        numReadsUnclassified=int(lines[-1].split(",")[3])
        abundanceUnclassified=numReadsUnclassified/numReads

        areport = open(sys.argv[3], "w")
        areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
        areport.write(str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified")

        for line in lines[1:-1]:
            l = line.split(",")
            hits = int(l[3])
            abundance = hits/numReads
            rank = get_rank(l[2])
            taxID = l[1]
            species_name=l[0]
            areport.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name))

