import sys

def get_rank(rank):
    rank_code = {'19': 'S', '18': 'G', '17': 'F', '16':'O', '15':'C', '14':'P', '13': 'K'}
    try:
        return rank_code[str(rank)]
    except KeyError:
        pass

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
    print("Usage: python ccmetagenOutput.py FILE.CLASSIFICATION FILE.REPORT NEW_FILE.areport")
else:
    unclassified=0
    with open (sys.argv[2], 'r') as report:
        lines=report.readlines()
        num_reads=0
        num_seq=len(lines)-1 # header
        for line in lines[1:]:
            l = line.split(",")
            num_reads+=l[1]
    print(num_reads)

    with open(sys.argv[1], "r") as classi:
        species = classi.readlines()
        #unclassified=int(species[-1].split(",")[3])
        #abundance_unclassified=unclassified/num_reads

        new_file = open(sys.argv[3], "w")
        new_file.write("Abundance\tnumReads\ttaxRank\ttaxID\tName\n")
        new_file.write(str(0)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")#new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified")
        hits=0
        for line in species[1:]:
            l = line.split(",")
            #hits = int(l[1])
            abundance = hits/num_reads
            for i in range(19, 12, -1):
                if not "unk" in l[i]:
                    rank=get_rank(i)
                    break
            taxID = l[11] #lca_taxid
            species_name=l[19]
            new_file.write("\n"+str(abundance)+"\t"+str(hits)+"\t"+str(rank)+"\t"+str(taxID)+"\t"+str(species_name))