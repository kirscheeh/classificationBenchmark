#!/usr/bin/env python
# translating kslam output into areport
import sys
import getting
def get_rank(name):
    try:
        rank_code = {'leaf':'L', 'subspecies': 'SP', 'strain': 'ST', 'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
        return rank_code[name]
    except KeyError:
        print("Key Error", name)
        return 0

if not len(sys.argv) == 4:
    print("An error occured.")
    print("Usage: python centrifugeOutput.py PATH/TO/file.CLASSIFICATION PATH/TOfile.REPORT PATH/TO/NEW_FILE.areport")
else:
    numReadsUnclassified=0
    with open (sys.argv[1], 'r') as classify: # vllt. kann ich das umgehen, wenn ich numReadsClassified mitrechne?
        lines=classify.readlines()
        
        for line in lines[1:]:
            if line.split("\t")[1] == "unclassified":
                    numReadsUnclassified +=1
    
    sample = getting.get_sampleName(sys.argv[1]) #number of lines in classificatoin file doesnt correspond to number of reads
    numReadsTotal = getting.get_numberReadsSample(sample)

    abundanceUnclassified=numReadsUnclassified/numReadsTotal

    areport = open(sys.argv[3], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    areport.write(str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified")
    unclassified_test=0
    with open(sys.argv[2], "r") as report:
        lines = report.readlines()

        for line in lines[1:]:
            l = line.split("\t")
            hits = int(l[4])
            unclassified_test+=hits
            abundance = hits/numReadsTotal
            rank = get_rank(l[2])            
            taxID = l[1]
            speciesName=l[0]
            if not rank == 0:
                areport.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(speciesName))
    
    print(unclassified_test)
