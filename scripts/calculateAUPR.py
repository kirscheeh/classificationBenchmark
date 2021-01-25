import sys, getting

def calculate_precision_recall(threshold, report):
    data=[]
    prediction=[]
    species =getting.get_species("../config.yaml")
    with open(report, 'r') as report:
        lines = report.readlines()
        num_spec=0
        pos=0
        neg = 0
        positives=[]
        for line in lines:
            line = line.split("\t")
            if line[3] == "S":
                num_spec +=1
                if float(line[0])>=float(threshold):
                    positives.append(line)
                    print(line)
                    pos +=1
                    name = str(line[-1].split(" ")[-2]+" "+line[-1].split(" ")[-1].split("\n")[0])
                    prediction.append(1)                           
                else:
                    neg+=1
                    prediction.append(0)
                if name in species:
                    data.append(1)
                else:
                    data.append(0)

    true_species = getting.get_species("../config.yaml")
    tp=0
    fp=0
    tn=0
    for hit in positives:
        splitted = hit[5].split(" ")
        name = splitted[len(hit[5].split(" "))-2]+" "+splitted[len(hit[5].split(" "))-1][:-1]

        if name in true_species:
            tp+=1
        else:
            fp+=1
    
        tn = num_spec-len(true_species)
        fn = len(true_species)-tp

    recall = tp/(tp+fn)
    precision=tp/(tp+fp)
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    #print(precision, recall, accuracy, threshold)
    return precision, recall, accuracy, threshold, prediction, data

def calcAUPR():
    threshold =sys.argv[1].split(" ")
    report = sys.argv[2]
    rec = [0]
    prec=[]
    result=[]
    for t in threshold:
        precision, recall, accuracy, thresh, h1, h2 = calculate_precision_recall(t, report)
        prec.append(precision)
        rec.append(recall)
        print(precision, recall, t)
        result.append(precision*abs(recall-rec[-1]))
    print(result)





if not len(sys.argv) == 3: 
    print("Something went wrong.")
    print("Usage: python calculateAUPR.python THRESHOLDs REPORT")
else:

    calcAUPR()
    #calculate_precision_recall()


"""import numpy as np
from sklearn.metrics import average_precision_score

h1, h2, h3, h4, p, d = calculate_precision_recall(sys.argv[1], sys.argv[2])
data=np.array(d)
pred=np.array(p)
#fpr, tpr, thresholds = metrics.roc_curve(data, pred, pos_label=2)
#metrics.auc(fpr, tpr)
average_precision = average_precision_score(pred, data)
print(average_precision)"""