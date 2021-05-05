import sys
import getting 
import numpy as np
import matplotlib.pyplot as plt
#from sklearn import metrics
from sklearn.metrics import average_precision_score

gt = getting.get_groundTruth(sys.argv[1])
ab = getting.get_abundances(sys.argv[1])



def calc_precision_recall(y_true, y_pred):
    TP=0
    FP=0
    FN=0
    TN=0
    for i in range(len(y_true)):
        #print(i)
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
    try:
        fpr = FP / (TN+FP)
    except:
        fpr = 1
    try:
        tpr = TP / (TP+FP)
    except:
        tpr = 1
    

    return precision, recall, tpr, fpr

#print(calc_precision_recall(test_true, test_pred))
precision_scores = []
recall_scores = []
tpr_scores=[]
fpr_scores=[]
probability_thresholds = np.linspace(0, 1, num=10000)

for p in probability_thresholds:
    y_test_preds=[]
    for prob in ab:
        if prob >= p:
            y_test_preds.append(1)
        else:
            y_test_preds.append(0)

    precicion, recall, tpr, fpr = calc_precision_recall(gt, y_test_preds)
    precision_scores.append(precicion)
    recall_scores.append(recall)
    tpr_scores.append(tpr)
    fpr_scores.append(fpr)


average_precision = average_precision_score(gt, ab)
print(average_precision)
#print(precision_scores[1:10], recall_scores[1:10])
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(recall_scores, precision_scores, label='Logistic Regression')
#baseline = len(gt[gt==1]) / len(gt)
#ax.plot([0, 1], [baseline, baseline], linestyle='--', label='Baseline')
ax.set_xlabel('Recall')
ax.set_ylabel('Precision')
plt.show()