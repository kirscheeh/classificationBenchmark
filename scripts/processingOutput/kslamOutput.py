import sys
from ete3 import NCBITaxa

def get_rank(taxid):
    rank_code = {'species': 'S', 'genus': 'G', 'family': 'F', 'order':'O', 'class':'C', 'phylum':'P', 'kingdom': 'K', 'superkingdom': 'D'}
    try:
        return rank_code[NCBITaxa().get_rank([int(taxid)])[int(taxid)]]
    except KeyError: #species group, strain, clade
       return "-"

if not len(sys.argv) == 3:
    print("An error occured.")
    print("Usage: python kslamOutput.py PATH/TO/file.CLASSIFICATION PATH/TO/NEW_FILE.areport")
else:
    abundance_unclassified=0
    unclassified=0
    new_file = open(sys.argv[2], "w")
    new_file.write("Abundace\tnumReads\ttaxRank\ttaxID\tName\n")
    new_file.write(str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified\n")

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        i=0
        total_reads_cl=0
        abundance_cl=0
        for line in lines:
            if "<taxon>" in line:
                numreads = lines[i+1].split("\"")[1]
                abundance=float(lines[i+1].split("\"")[2].split("<")[0][1:])/100
                taxid=lines[i+2].split(">")[1].split("<")[0]
                name=lines[i+4].split("name")[1][1:-2]
                rank=get_rank(int(taxid))
                new_file.write(str(abundance)+"\t"+numreads+"\t"+rank+"\t"+"\t"+name+"\n")
                total_reads_cl+=int(numreads)
                abundance_cl+=float(abundance)
            i+=1
        total_reads=total_reads_cl/abundance_cl
        unclassified=total_reads-total_reads_cl
        abundance_unclassified=1-abundance_cl
    new_file.close()
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()
        lines[1]=str(abundance_unclassified)+"\t"+str(unclassified)+"\t"+"U\t0\tunclassified\n"
    with open(sys.argv[2], 'w') as f:
        for line in lines:
            f.write(line)
