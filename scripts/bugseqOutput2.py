#!/usr/bin/env python

# translating bugseq output into areport
import sys
import getting
import glob

def get_rank(tax):
    rankCode = {'strain':'ST', 'subspecies':'SS', 'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', '2':'C', 'phylum':'P', 'kingdom': 'K'}
    try:
        return rankCode[str(tax)]
    except KeyError:
        return '-' #everything else

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python bugseqOutput.py classification-prefix new_file.areport")
else:
    if "366" in sys.argv[1]: # needs modification for other names
        sample="gridion366"
    else:
        sample="gridion364"
    
    gridion={}

    numReads= getting.get_numberReadsSample(sample)
    list_files = glob.glob(sys.argv[1]+"*.csv")
    for files in list_files:
        with open(files, "r") as report:
            lines = report.readlines()
            #numReadsUnclassified=int(lines[-1].split(",")[3])
            #abundanceUnclassified=numReadsUnclassified/numReads

            for line in lines[4:]:
                l = line.split("\t")
                print(l)
                hits = int(l[1])
                abundance = float(hits/numReads)
                rank = get_rank(str(l[4]))
                taxID = l[0]
                species_name=l[5].split("\n")[:-1][0]
                if taxID in gridion:
                    gridion[taxID][0] +=abundance
                    gridion[taxID][1] += hits
                else:
                    gridion[taxID]=[abundance, hits, rank, taxID, species_name]

areport = open(sys.argv[2], "w")
areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
#areport.write(str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified")
for entry in gridion.keys(): #except unclassificed, check that!
    entry_list = gridion[entry]
    areport.write("\n"+str(entry_list[0])+"\t"+str(entry_list[1])+"\t"+str(entry_list[2])+"\t"+str(entry_list[3])+"\t"+str(entry_list[4])) 


