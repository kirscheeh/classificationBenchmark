import sys 
import getting
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics


def calculate_precision_recall(threshold, report, config_path):
    data=[] # a bit redundant to calculate that again and again...
    prediction=[]
    
    # species in sample
    species =getting.get_species(config_path) #because run from main folder with snakefile
    
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
                    print(threshold, line)
        
                    positives.append(line)
                    pos +=1
                    
                    prediction.append(1)                           
                
                else:
                    print(threshold)
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
        #pass
        print("What")
        return 0


def calcAUPR_really(precision, recall):
    #print(len(precision), len(recall))
    return np.trapz(np.array(recall[1:]), x=np.array(precision))


def calcAUPR(threshold, report, config_path):
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
            precision, recall, accuracy, thresh, aupr = calculate_precision_recall(t, report, config_path)
            print("yes")
            aupr_list.append(aupr)
            print(aupr_list)
            #result.append(precision*abs(recall-rec[-1]))
            prec.append(precision)
            rec.append(recall)

      #  stats.write(str(t)+"\t"+str(precision)+"\t"+str(recall)+"\n")

        except Exception as e: # ??? ah, wenn nix über Grenze kommt, dann hab ich ne Exception weil 0
            print("here", e)
            tries+=1
            if tries >= 50: # maximum value plus 100
                return rec, prec, aupr_list, threshold
            #print("here No hits.")
        #print(result)
    return rec, prec, aupr_list, threshold

print(calcAUPR([0.6, 0.7, 0.8, 0.9, 1], sys.argv[1], sys.argv[2]))

def plotting(recall, precision, aupr, threshold, areport, asp):

    #fig, (ax1, ax2) = plt.subplots(2)
    plt.plot(rec[1:], prec)
    plt.title(str(areport)+"\nAUPRC:"+str(round(aupr, 5))+"\nASP:"+str(asp))
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xticks(ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    #print(aupr)
    #ax2.plot(aupr, th)
    plt.show()


"""if not len(sys.argv) == 3: 
    print("Something went wrong.")
    print("Usage: python calculateAUPR.python REPORT CONFIG.YAML")
else:
    print(sys.argv)
    th = [i*0.001 for i in range(0, 100001)]
    rec, prec, aupr, th = calcAUPR(th, sys.argv[1], sys.argv[2])#sys.argv[1].split(" ")
    #aupr = calcAUPR_really(prec, rec)
    #if "kraken2" in sys.argv[2] or "clark" in sys.argv[2]:
        
    truth=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.02, 0.02]
    #else:
    #    truth=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12] #currently no fungi
    asp = getting.get_ASP(sys.argv[2], truth)
    #plotting(rec, prec, aupr, th, sys.argv[2], asp)"""
    
