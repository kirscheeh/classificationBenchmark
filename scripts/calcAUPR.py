import sys
import getting
import sklearn.metrics
import math
import warnings
import matplotlib.pyplot as plt

def getGroundTruth(report):
    # calculates the number of TP
    data=[]
    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line=line.split("\t")

            # is it an species entry and is the species in the sample?
            if line[2] == "S":
                if line[4].split("\n")[0] in species:  
                    data.append(1)
                else:
                    data.append(0)
    return data

def getPrediction(threshold, report):
    # for a given threshold, calculate the Positives and Negatives
    num_species=0
    positive_spec=[]
    negative_spec=[]
    prediction=[]
    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line = line.split("\t")
            if line[2]=="S":
                num_species+=1

                if float(line[0]) >= float(threshold):
                    positive_spec.append(line)
                    prediction.append(1)
                else:
                    prediction.append(0)
    return prediction

def calcFalsePositives(prediction, groundTruth):
    # calculates precision and recall and AUPR for a TH
    tp=0
    tn=0
    for i in range(len(prediction)):
        if prediction[i]==groundTruth[i]:
            if groundTruth[i] == 1:
                tp+=1
            else:
                tn+=1
    fp =sum(prediction)-tp
    fn = len(prediction)-sum(prediction)-tn
    return tp, fp, tn, fn

def calcPrecision(tp, fp, tn, fn):
    # for given tp, fp, tn, fn values, calculate precision
    try:
        return tp/(tp+fp)
    except ZeroDivisionError as e:
        #print("No precision possible:", e)
        print(tp, fp)
        return 0

def calcRecall(tp, fp, tn, fn):
    # for given tp, fp, tn, fn values, calculate recall
    try:
        return tp/(tp+fn)
    except ZeroDivisionError as e:
        print(tp, fn)
        #print("No recall possible.", e)
        return 0

def calcAccuracy(tp, fp, tn, fn):
    # for a given tp, fp, tn, fn, calculate accuracy
    try:
        return (tp+tn)/(tp+tn+fp+fn)
    except ZeroDivisionError as e:
        #print("No accuracy possible.", e)
        print(tp, fp, tn, fn)
        return 0

def calcOneAUPR(prediction, groundTruth):
    # for a given th
    return sklearn.metrics.average_precision_score(prediction, groundTruth)

def calcAUPRCurve(threshold, report, stats):
    groundTruth=getGroundTruth(report)
    precisions=[]
    recalls=[]
    auprs=[]
    new_file = open(stats, 'w')
    new_file.write("Threshold\tPrecision\tRecall\tAUPR\n")
    tries=0 # at one point, nothing will be over the threshold anymore
    for th in threshold:
        prediction = getPrediction(th, report)
        tp, fp, tn, fn = calcFalsePositives(prediction, groundTruth)
        try:
            prec=calcPrecision(tp, fp, tn, fn)
            precisions.append(prec)
            
            rec=calcRecall(tp, fp, tn, fn)
            recalls.append(rec)
            
            aupr=calcOneAUPR(prediction, groundTruth)
            auprs.append(aupr)
            warnings.filterwarnings('ignore')
            
            if math.isnan(aupr):
                tries+=1
                if tries>=100:
                    return 0
            
            new_file.write(str(th)+"\t"+str(prec)+"\t"+str(rec)+"\t"+str(aupr)+"\n")
        except TypeError as e: 
            pass
    
def plotting(stats="", precision=[], recall=[], auprs=[]):
    if not precision or not recall or not auprs:
        if not stats=="":
            with open(stats, 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    print(line)
                    line=line.split("\t")
                    precision.append(line[1])
                    recall.append(line[2])
                    auprs.append(line[3])
        else:
            print("No values, no file. That won't work.")
    plt.plot(recall[1:], precision[1:])
    #plt.title(str(areport)+"\nAUPRC:"+str(round(aupr, 5))+"\nASP:"+str(asp))
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xticks(ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.show()
    

if not len(sys.argv)==4:
    print("Wrong number of arguments!")
    print("python calcAUPR.py PATH/TO/AREPORT PATH/TO/CONFIG PATH/TO/NEW/STATS")
else:
    species = getting.get_species(sys.argv[2])
    groundTruth=getGroundTruth(sys.argv[1])
    calcAUPRCurve([i*0.001 for i in range(0, 100001)], sys.argv[1], sys.argv[4])

#plotting(stats="../stats/gridion364_default.kaiju.stats")