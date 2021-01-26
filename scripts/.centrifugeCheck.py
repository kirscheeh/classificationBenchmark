import sys

reads=0
reads_u=0
with open(sys.argv[1], 'r') as report:
    species = report.readlines()
    for line in species[1:]:
        #print(line.split("\t"))
        reads_u += int(line.split("\t")[5])
        reads += int(line.split("\t")[4])

print("Unique:", reads_u)
print("All:", reads)