# translating kraken2 output into areport
import sys
import getting

def get_name(name_long): # scientific name
    name_list = name_long.split(" ")
    name_list[-1]=name_list[-1].split("\t")[0]
    name=""
    for elem in name_list:
        if not elem == "":
            if elem == name_list[-1]:
                name+=elem
            else:
                name +=elem+" "
    return name

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python krakenOutput.py file.report new_file.areport")
else:
    
    areport = open(sys.argv[2], "w")
    areport.write("Abundance\tnumReads\ttaxRank\ttaxID\tName")

    with open(sys.argv[1], "r") as report:
        lines = report.readlines()
        
        numReadsUnclassified = lines[0].split("\t")

        sample=getting.get_sampleName(sys.argv[1])
        numReadsTotal =getting.get_numberReadsSample(sample)

        areport.write("\n"+str(float(numReadsUnclassified[0])/100)+"\t"+str(numReadsUnclassified[1])+"\t"+"U\t0\tunclassified\n")
        
        for line in lines[1:]:
            l = line.split("\t")
            rank=l[3]
            hits=int(l[1])
            abundance=hits/numReadsTotal
            taxID = l[4]
            speciesName=get_name(l[5])
            
            areport.write(str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(speciesName))
    
                
