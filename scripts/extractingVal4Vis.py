# script for extracting ground truth and abundances of species for given areport
# parameter needed: areport
import sys
import getting 

gt = getting.get_groundTruth(sys.argv[1])
ab = getting.get_abundances(sys.argv[1])

with open(sys.argv[2], 'w+') as f:
    f.write("gt\tab\n")
    for i in range(len(gt)):
        f.write(str(gt[i])+"\t"+str(ab[i])+"\n")
