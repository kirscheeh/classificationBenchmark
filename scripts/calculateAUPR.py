#!/usr/bin/python

# This script calculates the area under a precision-recall curve for two given lists as input
#
# @Kirsten

import numpy as np
import argparse

### CLI ###
parser = argparse.ArgumentParser(description='Calculate the AUPR.')
parser.add_argument('labels', metavar='labels', 
                    help='the reference labels for the given task (comma-separated list!)')
parser.add_argument('predictions', metavar='predictions', 
                    help='the predicitons the classifier produced (comma-separated list!)')
args = parser.parse_args()
### CLI END ###

def getValues(file):
    with open (file, 'r') as f:
        content = f.readline()
        result = content.split(",")
        for elem in result:
            elem = float(elem)
        return result

# copied from https://towardsdatascience.com/how-to-efficiently-implement-area-under-precision-recall-curve-pr-auc-a85872fd7f14
predictions = np.array(getValues(args.predictions), dtype=float)
#labels = np.array(getValues(args.labels), dtype=float)
#predictions = np.array([0.65,0.1,0.15,0.43,0.97,0.24,0.82,0.7,0.32,0.84])
labels = np.array([12, 12, 12, 12, 12, 12, 12, 12, 2, 2])


# sort the entries according to the predicted confidence
id = np.argsort(predictions)[::-1]
predictions = predictions[id]
labels = labels[id]

cumsum = np.cumsum(labels)
rank = np.arange(len(cumsum)) + 1
Num = cumsum[-1]
prec = cumsum / rank
rec = cumsum / Num

mrec = np.concatenate(([0.], rec, [1.]))
mpre = np.concatenate(([0.], prec, [0.]))

# compute the precision envelope
for i in range(mpre.size - 1, 0, -1):
    mpre[i - 1] = np.maximum(mpre[i - 1], mpre[i])

i = np.where(mrec[1:] != mrec[:-1])[0]

pr_auc = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])

print(pr_auc)