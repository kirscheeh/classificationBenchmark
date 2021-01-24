import sys, getting

if not len(sys.argv) == 3: 
    print("Something went wrong.")
    print("Usage: python calculateAUPR.python THRESHOLD REPORT")
else:
    threshold = sys.argv[1]
    with open(sys.argv[2], 'r') as report:
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
                else:
                    neg+=1

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
print(precision, recall, accuracy, threshold)