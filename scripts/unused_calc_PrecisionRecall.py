# calculating the area under precision recall curve
import sys
import getting
#import sklearn.metrics
#import warnings
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

def get_groundTruth(report): # ground truth vector based on species level
    data=[]

    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line=line.split("\t")

            if line[2]=="S":
                if line[4].split("\n")[0] in species:  
                    data.append(1)
                else:
                    data.append(0)
            #else:
                #data.append(0)
    #print(len(data), sum(data))
    return data

def get_prediction(threshold, report, abundance=False): # for a given threshold, returns suspected true classifications
    prediction=[]
    
    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line = line.split("\t")

            
            if "S" == line[2]:
                if abundance:
                    if float(line[0]) >= float(threshold):
                        prediction.append(float(line[0]))
                    else:
                        prediction.append(0)

                else:
                    if float(line[0]) >= float(threshold):
                        prediction.append(1)
                        if threshold==0.003:
                            print(line)
                    else:
                        prediction.append(0)
                
            """else:
                if abundance:
                    prediction.append(float(line[0]))
                else:
                    prediction.append(0)"""
    #print(len(prediction), sum(prediction))
    return prediction

def calc_matrixOfConfusion(prediction, groundTruth):
    # calculates TP, FP, TN and FN for a given prediction, i.e. threshold 
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

def calc_precision(tp, fp, tn, fn):
    try:
        return tp/(tp+fp)
    except ZeroDivisionError as e:
        return 0

def calc_recall(tp, fp, tn, fn):
    try:
        return tp/(tp+fn)
    except ZeroDivisionError as e:
        return 0

def calc_fpr(tp, fp, tn, fn): # not used
    # calculate false positive rate
    try:
        return fp/(tn+fp)
    except ZeroDivisionError:
        return 0

def calc_accuracy(tp, fp, tn, fn):
    try:
        return (tp+tn)/(tp+tn+fp+fn)
    except ZeroDivisionError as e:
        return 0

#def calcOneAUPR_binary(prediction, groundTruth):
#    return sklearn.metrics.average_precision_score(prediction, groundTruth)

#def calcOneAUPR_abundance(prediction_abundance, groundTruth):
 #   # for a given th
#    return sklearn.metrics.average_precision_score(groundTruth, prediction_abundance)

def calc_prCurve(threshold, report, stats):
    precisions=[]
    recalls=[]
    auprs_bin=[]
    auprs_pred=[]
    
    new_file = open(stats, 'w')
    new_file.write("Threshold\tPrecision\tRecall\n")
    
    tries=0 # at one point, nothing will be over the threshold anymore
    for th in threshold:
        prediction = get_prediction(th, report)
        tp, fp, tn, fn = calc_matrixOfConfusion(prediction, groundTruth)
        try:
            prec=calc_precision(tp, fp, tn, fn)
            precisions.append(prec)
            
            rec=calc_recall(tp, fp, tn, fn)
            recalls.append(rec)

            new_file.write(str(th)+"\t"+str(prec)+"\t"+str(rec)+"\n")
            
            if prec == 0 and rec == 0:
                tries+=1
                if tries>=50:
                    return threshold, precisions, recalls

        except TypeError as e: 
            pass
    return threshold, precisions, recalls
    
def calc_aupr(precision): # reurns area under precision recall curve
    return np.trapz(precision, dx=0.00001), simps(precision, dx=0.00001)
 
def filter(precision, recall):
    values={precision[i]:[] for i in range(len(precision))}
    for i in range(len(precision)):
        values[precision[i]].append(recall[i])
    
    for elem in values.keys():
        values[elem]=max(values[elem])
    unused=values.pop(0.0)
    #print(values)
    values[1.0]=0
    #print(unused)
    print(values)
    return list(values.keys()),list(values.values())

def plot_prCurve(stats="", precision=[], recall=[]):
    if not precision or not recall:
        if not stats=="":
            try:
                with open(stats, 'r') as file:
                    lines = file.readlines()
                    for line in lines[1:]:
                        line=line.split("\t")
                        precision.append(float(line[1]))
                        recall.append(float(line[2]))
            except FileNotFoundError:
                print("No values, no file. That won't work.")
        else:
            print("No values, no file. That won't work.")
    #precision, recall = filter(precision, recall)
    #plt.plot(recall, precision)
    #plt.title("gridion364_quals.centrifuge.areport")
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xticks([0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9, 1])
    plt.yticks([0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8, 0.9, 1])
    print(calc_aupr(precision))
    #plt.show()
    

if not len(sys.argv)==5:
    print("Wrong number of arguments!")
    print("python calcAUPR.py PATH/TO/AREPORT PATH/TO/CONFIG PATH/TO/NEW/STATS [True|False]")
    print("Last parameter is for plotting the PR-Curve.")
else:
    species = getting.get_species(sys.argv[2])
    groundTruth=get_groundTruth(sys.argv[1])
    calc_prCurve([i*0.00001 for i in range(1, 10000001)], sys.argv[1], sys.argv[3])
    if sys.argv[4] in ["True", "true"]:
        plot_prCurve(stats=sys.argv[3])

#species =getting.get_species(sys.argv[2])
#groundTruth=get_groundTruth(sys.argv[1])
#calc_prCurve([i*0.001 for i in range(1, 100001)], sys.argv[1], sys.argv[3])
#plot_prCurve(stats=sys.argv[3])

#TODO
# testing this script!


