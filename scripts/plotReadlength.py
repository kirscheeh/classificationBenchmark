import getting as get
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

f = sys.argv[1]

seq = get.get_sequences(f)
medianLength = get.get_seqLength(f)
print(medianLength)

plt.hist([len(i) for i in seq], bins=1000)
plt.ylabel("abundance")
plt.xlabel("read length")
plt.savefig(sys.argv[2], transparent=True)
