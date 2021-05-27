# translating centrifuge output into areport
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
    print("Usage: python centrifugeOutput.py file.classification file.REPORT file.areport")
else:
    numReadsUnclassified=0
    with open (sys.argv[1], 'r') as classify: # centrifuge assigns a read to more than one species, therefore number of total assignments is important
        lines=classify.readlines()
        
        for line in lines[1:]:
            if line.split("\t")[1] == "unclassified":
                    numReadsUnclassified +=1
        numberAssignments=len(lines)-1 # due to header
    sample = getting.get_sampleName(sys.argv[1]) 

    abundanceUnclassified=numReadsUnclassified/numberAssignments

    areport = open(sys.argv[3], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
    areport.write(str(abundanceUnclassified)+"\t"+str(numReadsUnclassified)+"\t"+"U\t0\tunclassified") 
    
    with open(sys.argv[2], "r") as report:
        lines = report.readlines()

        for line in lines[1:]:
            l = line.split("\t")
            hits = int(l[4])
            abundance = hits/numberAssignments
            rank = get_rank(l[2])            
            taxID = l[1]
            speciesName=l[0]

            if not rank == 0: # rank 0: read unclassified or assigned to irrelevant taxonomic rank
                areport.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(speciesName))
    areport.close()