import sys 
import getting
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics


def calculate_precision_recall(threshold, report):

    data=[] # a bit redundant to calculate that again and again...
    prediction=[]
    
    # species in sample
    species =getting.get_species("../config.yaml") #because run from main folder with snakefile
    
    with open(report, 'r') as report:
        lines = report.readlines()
        number_species=0
        
        pos=0 # above threshold
        neg = 0 # below threshold
        positives=[] # meaning above threshold
        
        for line in lines:
            line = line.split("\t")
            
            if line[2] == "S": #species level
                
                name=line[4].split("\n")[0]
                #print(line[0])
                number_species +=1
                
                if float(line[0])>=float(threshold):
        
                    positives.append(line)
                    pos +=1
                    
                    prediction.append(1)                           
                
                else:
                    neg+=1
                    prediction.append(0)
                
                if name in species: # regardless of limit because GT
                    data.append(1)
                else:
                    data.append(0)

    tp=0
    fp=0
    tn=0
    fn=0
    for hit in positives:
        name=hit[4].split("\n")[0]
        if name in species:
            tp+=1
        else:
            fp+=1
    tn = number_species-len(species)
    fn = len(species)-tp
    try:
        recall = tp/(tp+fn)
        precision=tp/(tp+fp)
        accuracy = (tp+tn)/(tp+tn+fp+fn)
        aupr = sklearn.metrics.average_precision_score(prediction, data)
        
        return precision, recall, accuracy, threshold, aupr
    
    except ZeroDivisionError:
        pass
        return 0

def calcAUPR_really(precision, recall):
    #print(len(precision), len(recall))
    return np.trapz(np.array(recall[1:]), x=np.array(precision))

def calcAUPR(threshold, report):
    tries=0
    sample_name=report.split("/")[-1][:-7]
    rec = [0]
    prec=[]
    result=[]
    aupr_list=[]

    stats = open("../stats/"+str(sample_name)+"stats", "w")
    stats.write("Threshold\tPrecision\tRecall\n")
    
    for t in threshold:
        
        try:
            
            precision, recall, accuracy, thresh, aupr = calculate_precision_recall(t, report)
            aupr_list.append(aupr)
            #result.append(precision*abs(recall-rec[-1]))
            prec.append(precision)
            rec.append(recall)

            stats.write(str(t)+"\t"+str(precision)+"\t"+str(recall)+"\n")

        except Exception:
            tries+=1
            if tries >= 100: # maximum value plus 100
                return rec, prec, aupr_list, threshold
            #print("here No hits.")
        #print(result)
    return rec, prec, aupr_list, threshold

def plotting(recall, precision, aupr, threshold):

    #fig, (ax1, ax2) = plt.subplots(2)
    plt.plot(rec[1:], prec)
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xticks(ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    #print(aupr)
    #ax2.plot(aupr, th)
    plt.show()


if not len(sys.argv) == 3: 
    print("Something went wrong.")
    print("Usage: python calculateAUPR.python THRESHOLDs REPORT")
else:
    th = [i*0.001 for i in range(0, 100001)]
    rec, prec, aupr, th = calcAUPR(th, sys.argv[2])#sys.argv[1].split(" ")
    plotting(rec, prec, aupr, th)
    print(calcAUPR_really(prec, rec))

#"0.01 0.011 0.012 0.013 0.014 0.015 0.016 0.017 0.018 0.019 0.02 0.021 0.022 0.023 0.024 0.025 0.026 0.027 0.028 0.029 0.03 0.031 0.032 0.033 0.034 0.035 0.036 0.037 0.038 0.039 0.04 0.041 0.042 0.043 0.044 0.045 0.046 0.047 0.048 0.049 0.05 0.051 0.052 0.053 0.054 0.055 0.056 0.057 0.058 0.059 0.06 0.061 0.062 0.063 0.064 0.065 0.066 0.067 0.068 0.069 0.07 0.071 0.072 0.073 0.074 0.075 0.076 0.077 0.078 0.079 0.08 0.081 0.082 0.083 0.084 0.085 0.086 0.087 0.088 0.089 0.09 0.091 0.092 0.093 0.094 0.095 0.096 0.097 0.098 0.099 0.1 0.11 0.12 0.13 0.14 0.15"
"""import numpy as np
from sklearn.metrics import average_precision_score

h1, h2, h3, h4, p, d = calculate_precision_recall(sys.argv[1], sys.argv[2])
data=np.array(d)
pred=np.array(p)
#fpr, tpr, thresholds = metrics.roc_curve(data, pred, pos_label=2)
#metrics.auc(fpr, tpr)
average_precision = average_precision_score(pred, data)
print(average_precision)"""