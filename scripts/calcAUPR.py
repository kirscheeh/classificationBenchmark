import sys
import getting
import sklearn.metrics
import math
import warnings
import matplotlib.pyplot as plt

def getGroundTruth(report):
    # calculates the number of TP
    data=[]
    i=0
    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line=line.split("\t")

            # is it an species entry and is the species in the sample?
            if "S" in line[2]:
                i+=1
                #print(i)
                if line[2]=="S":
                    if line[4].split("\n")[0] in species:  
                        data.append(1)
                    else:
                        data.append(0)
                else:
                    for s in species:
                        if s in line[4].split("\n")[0]:
                            print(line)
                            data.append(1)
                            break
                    else:
                        data.append(0)
    print(i)
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
            if "S" in line[2]:
                num_species+=1
                if float(line[0]) >= float(threshold):
                    positive_spec.append(line)
                    prediction.append(1)
                else:
                    prediction.append(0)
    print(len(prediction))
    return prediction

def getAbundances(report):
    abundances=[]
    with open(report, 'r') as report:
        lines=report.readlines()
        counter=0
        for line in lines[1:]:
            line = line.split("\t")
            if "S" in line[2]: #line[2]=="S"
                abundances.append(float(line[0]))
    #print(len(abundances))
    return abundances


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
        #print(tp, fp)
        return 0

def calcRecall(tp, fp, tn, fn):
    # for given tp, fp, tn, fn values, calculate recall
    try:
        return tp/(tp+fn)
    except ZeroDivisionError as e:
        #print(tp, fn)
        #print("No recall possible.", e)
        return 0

def calcFPR(tp, fp, tn, fn):
    # calculate false positive rate
    try:
        return fp/(tn+fp)
    except ZeroDivisionError:
        return 0
def calcAccuracy(tp, fp, tn, fn):
    # for a given tp, fp, tn, fn, calculate accuracy
    try:
        return (tp+tn)/(tp+tn+fp+fn)
    except ZeroDivisionError as e:
        #print("No accuracy possible.", e)
        #print(tp, fp, tn, fn)
        return 0

def calcOneAUPR_binary(prediction, groundTruth):
    # for a given th
    return sklearn.metrics.average_precision_score(prediction, groundTruth)

def calcOneAUPR_abundance(prediction_abundance, groundTruth):
    # for a given th
    return sklearn.metrics.average_precision_score(groundTruth, prediction_abundance)
def calcFPR(tp, fp, tn, fn):
    try:
        return fp/(fp+tn)
    except Exception:
        return 0
def calcAUPRCurve(threshold, report, stats):
    #groundTruth=getGroundTruth(report)
    precisions=[]
    recalls=[]
    auprs_bin=[]
    auprs_pred=[]
    new_file = open(stats, 'w')
    new_file.write("Threshold\tPrecision\tRecall\tAUPR_bin\tAUPR_pred\n")
    tries=0 # at one point, nothing will be over the threshold anymore
    for th in threshold:
        prediction = getPrediction(th, report)
        tp, fp, tn, fn = calcFalsePositives(prediction, groundTruth)
        abundances=getAbundances(report)
        try:
            prec=calcPrecision(tp, fp, tn, fn)
            precisions.append(prec)
            
            rec=calcRecall(tp, fp, tn, fn)
            recalls.append(rec)
            
            aupr_bin=calcOneAUPR_binary(prediction, groundTruth)
            auprs_bin.append(aupr_bin)
            
            aupr_pred=calcOneAUPR_abundance(abundances, groundTruth)
            auprs_pred.append(aupr_pred)
            
            warnings.filterwarnings('ignore')
            
            if math.isnan(aupr_bin):
                tries+=1
                if tries>=100:
                    return 0
            
            new_file.write(str(th)+"\t"+str(prec)+"\t"+str(rec)+"\t"+str(aupr_bin)+"\t"+str(aupr_pred)+"\n")
        except TypeError as e: 
            pass
    
def plotting(stats="", precision=[], recall=[], auprs=[]):
    if not precision or not recall or not auprs:
        if not stats=="":
            with open(stats, 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    line=line.split("\t")
                    if not math.isnan(float(line[3])):# and not line[2]=="0.0" and not line[1]=="0.0":
                    #print(line)
                        precision.append(float(line[1]))
                        recall.append(float(line[2]))
                        auprs.append(float(line[3]))
                    else:
                        break
        else:
            print("No values, no file. That won't work.")
   # print(precision[1:5])
    #precision.reverse()
    #print(precision[1:5])

    recall.reverse()
    precision.reverse()
    #auprs.reverse()
    #auprs_1=calcOneAUPR_abundance(groundTruth, precision)
    print(auprs)
   # plt.plot(recall, precision)#recall[1:], precision[1:])
    plt.plot(recall, precision)
    plt.title("gridion366_default.kaiju.areport")
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xticks([0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9, 1])
    plt.yticks([0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9, 1])

    from numpy import trapz
    print(trapz(precision, dx=0.001))
    plt.show()
    

"""if not len(sys.argv)==4:
    print("Wrong number of arguments!")
    print("python calcAUPR.py PATH/TO/AREPORT PATH/TO/CONFIG PATH/TO/NEW/STATS")
else:
    species = getting.get_species(sys.argv[2])
    groundTruth=getGroundTruth(sys.argv[1])
    calcAUPRCurve([i*0.001 for i in range(0, 100001)], sys.argv[1], sys.argv[3])"""
species = getting.get_species(sys.argv[2])
groundTruth=getGroundTruth(sys.argv[1])
calcAUPRCurve([i*0.001 for i in range(1, 100001)], sys.argv[1], sys.argv[3])
plotting(stats=sys.argv[3])

