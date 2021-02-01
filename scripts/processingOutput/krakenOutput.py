import sys

def check_rank(rank):
    if rank in ["S", "G", "F", "O", "C", "P", "K", "D"]:
        return True
    else:
        return False

def get_name(name_long):
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
    print("Usage: python krakenOutput.py file.REPORT NEW-FILE.areport")
else:
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName")
    with open(sys.argv[1], "r") as report:
        species = report.readlines()
        unclassified = species[0].split("\t")
        num_reads=int(unclassified[1])+int(species[1].split("\t")[1])
        print(num_reads)
        new_file.write("\n"+str(float(unclassified[0])/100)+"\t"+str(unclassified[1])+"\t"+"U\t0\tunclassified\n")
        for line in species[1:]:
            l = line.split("\t")
            rank=l[3]
            #if check_rank(rank):
            hits=int(l[1])
            abundance=hits/num_reads
            taxID = l[4]
            species_name=get_name(l[5])
            new_file.write(str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name))
                