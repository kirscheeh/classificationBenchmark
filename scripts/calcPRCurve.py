# validation script for PR-Curve and AUC with python and sklearn
import sys
import getting 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score

try: 
    areport = sys.argv[1]
    output = sys.argv[2]

    title = areport.split("/")[-1] #for png
except IndexError:
    print("Wrong number of arguments!")
    print("Usage: python calcPRCurve.py file.areport output.png")
    exit()

gt = getting.get_groundTruth(sys.argv[1])
ab = getting.get_abundances(sys.argv[1])


def calc_precision_recall(y_true, y_pred):
    TP=0
    FP=0
    FN=0
    TN=0
    for i in range(len(y_true)):
        if y_true[i]==1 and 1==y_pred[i]:
            TP+=1
        if y_true[i]==0 and y_pred[i]==1:
            FP+=1
        if y_true[i]==1 and y_pred[i]==0:
            FN+=1
        if y_true[i]==0 and y_pred[i]==0:
            TN+=1
    try:
        precision = TP / (TP+FP)
    except:
        precision = 1
    try:
        recall = TP / (TP+FN)
    except:
        recall = 1
    
    return precision, recall

precision_scores = []
recall_scores = []

probability_thresholds = np.linspace(0, 1, num=10000) # number of steps for threshold

for p in probability_thresholds: # for each threshold, get binary vector if entry is considered as true
    y_test_preds=[]
    for prob in ab:
        if prob >= p:
            y_test_preds.append(1)
        else:
            y_test_preds.append(0)

    precicion, recall = calc_precision_recall(gt, y_test_preds)
    precision_scores.append(precicion)
    recall_scores.append(recall)



average_precision = average_precision_score(gt, ab)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(recall_scores, precision_scores, label='')

baseline = sum(gt) / len(gt)
ax.plot([0, 1], [baseline, baseline], linestyle='--', label='Baseline')

ax.set_xlabel('Recall')
ax.set_ylabel('Precision')
plt.title(str(title)+"\nAUC= "+str(average_precision))
plt.savefig(output)