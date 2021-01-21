import getting as get
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

f = sys.argv[1]
maxi = 0
mini=1000000
seq = get.get_sequences(f)

for elem in seq:
    if len(elem)>maxi:
        maxi=len(elem)
    if len(elem) < mini:
        mini=len(elem)

medianLength = get.get_seqLength(f)
averageLength = get.get_seqLength(f, True, False)
#print(medianLength, averageLength)

nameList = sys.argv[1].split("/")
name = nameList[len(nameList)-1]

plt.hist([len(i) for i in seq], bins=1000)
plt.ylabel("abundance")
plt.xlabel("read length")
#plt.xticks([i for i in range(round(mini, -3), round(maxi, -3)+1000, 2000)])
#plt.xlim(right=25000)
plt.title("Distribution of read lengths for "+str(name))
plt.figtext(.6, .7,"\nMedian length: "+str(medianLength)+"\nAverage length: "+str(averageLength)+"\nShortest sequence: "+str(mini)+"\nLongest sequence: "+str(maxi))

plt.savefig(sys.argv[2], transparent=False)
