import getting 
import numpy as np
import sys
from scipy.spatial import distance

 #caclulates abundance profile similarities, either between truth and tool output or between tools

areport=sys.argv[1]
#truth=sys.argv[2]
config=sys.argv[2]

    
predi = getting.get_abundanceSampleSpecies(areport, config).values()
pred=list(predi)

sampleName = getting.get_sampleName(areport)

if sampleName =="gridion364":
    truth=[0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928,0.0192, 0.0178]
    #get_APS(areport, truth=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.02, 0.02], printing=True)
elif sampleName=="promethion365":
    truth=[0.1902, 0.1433, 0.1207, 0.1111, 0.1032, 0.1026, 0.1011, 0.0913,0.0187, 0.0177]
else: #gridion366, promethion367
    truth=[0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089]

try:
    t = np.array(truth)
    p = np.array(pred)
    l20 = np.sum(np.power((t-p),2))
    l21 = distance.euclidean(t, p)


    #print(areport.split("/")[-1])
    print(areport, "l20 nope", l20)
    print(areport, "l21", l21)
    #eturn l2
except Exception as e:
    print("An error occured.", e)

# CS even:
# measured [0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928, 0.0192, 0.0178]
# expected [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.02, 0.02]
# CS log:
# expected: [0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089]