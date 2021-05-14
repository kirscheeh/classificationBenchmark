#!/usr/bin/env python
# calculating abundance profile similarities with L2 distance and scipy

import getting 
import numpy as np
import sys
from scipy.spatial import distance

try:
    areport=sys.argv[1]
    config=sys.argv[2]
except IndexError:
    print("Wrong number of arguments!")
    print("Usage: python abundanceProfileSimilarity.py file.areport config.yaml")
    exit()

    
predi = getting.get_abundanceSampleSpecies(areport, config).values()
pred=list(predi)

sampleName = getting.get_sampleName(areport)
toolName =getting.get_toolsClassification(config)


taxids = getting.get_taxIDs(getting.get_species(config)) 

# using the estimated abundances of Nicholls et al. [14]
if sampleName =="gridion364":
    truth=[0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928,0.0192, 0.0178]
elif sampleName=="promethion365":
    truth=[0.1902, 0.1433, 0.1207, 0.1111, 0.1032, 0.1026, 0.1011, 0.0913,0.0187, 0.0177]
else: #gridion366, promethion367 --> expected abundances
    truth=[0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089]

try:
    if "default" in sys.argv[1]: # because if fungi: except for Kraken2, those abundances are not considered
        if toolName == "kraken2":
            t = np.array(truth)
            p = np.array(pred)
        else:
            t = np.array(truth[:-2])
            p = np.array(pred[:-2])
    else: # custom database, all species are considered
        t = np.array(truth)
        p = np.array(pred)

    l2 = distance.euclidean(t, p)


    print(areport+str(", APS:"), l2)
    #eturn l2
except Exception as e:
    print("An error occured.", e)
