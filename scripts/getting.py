#!/usr/bin/env python
# Script with several useful functions needed across the different scripts
import os, yaml, sys
import numpy as np
from numpy import array
from numpy.linalg import norm
# from scipy.spatial import distance

def get_species(config): # expected species in sample
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c) 
            species = parsed_yaml['species']
        return species
    else:
        print('Error! No config file', config)

print(os.getcwd())
config='config.yaml'
species = get_species(config)

def get_path(config): #get path to working directory
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            path = parsed_yaml['path']
        return path
    else:
        print('Error! No config file', config)

def get_dataIndices(config): # return path to database
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            index = parsed_yaml['dataIndex']
        return index
    else:
        print('Error! No config file', config)

def get_samples(config): # returns list of samples
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            samples = parsed_yaml['samples']
            return samples
    else:
        print('Error! No config file', config)

def get_numberSpecies(areport): # returns classified taxa on species level
    number=0
    with open(areport, "r") as report:
        lines = report.readlines()
        print(len(lines))
        for line in lines:
            if line.split("\t")[2] == "S":
                number+=1
    return number

def get_toolsClassification(config): # returns classification tools
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            tools = parsed_yaml['classification']
        return tools
    else:
        print('Error! No config file', config)

def get_abundanceSampleSpecies(areport, config): #returns abundance of expected species
    species = get_species(config)
    #predictions={sp:0 for (sp, 0) in species}

    for s in species:
        # grepping entries that include species name
        os.system('grep -n "{spec}" {file} > helping.log'.format(file=areport, spec=s))
        with open('helping.log', 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.split("\t")
                if line[4][:-1] == s and line[2]=="S": # species level
                    predictions[s] = float(line[0].split(":")[1])

            
            if not s in predictions: # if no fitting entry is found, filling with 0
                predictions[s]=0
                
        os.system('rm helping.log')
    
    #print(list(predictions.values()))
    return predictions

def get_APS(areport, truth, config=config, tool=False, printing=False): #caclulates abundance profile similarities, either between truth and tool output or between tools
    
    predi = get_abundanceSampleSpecies(areport, config).values()
    pred=list(predi)

    if tool:
        try:
            t = get_abundanceSampleSpecies(truth, config).values()
            truth=list(t)
        except:
            pass
            return 0
    sampleName = get_sampleName(areport)
    if sampleName in ['gridion364', 'promethion365']:
        truth=[0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928, 0.0192, 0.0178]
        get_APS(areport, truth=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.02, 0.02], printing=True)
    else:
        truth=[0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089]

    try:
        t = np.array(truth)
        p = np.array(pred)
        l2 = np.sum(np.power((t-p),2))
        # l2 = distance.euclidean(t, p)

        if printing:
            print(areport.split("/")[-1], l2)
        return l2
    except Exception as e:
        print("An error occured.", e)

# CS even:
# measured [0.1932, 0.1456, 0.1224, 0.1128, 0.0999, 0.0993, 0.097, 0.0928, 0.0192, 0.0178]
# expected [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.02, 0.02]
# CS log:
# expected: [0.0089, 0.891, 0.0000089, 0.00000089, 0.00089, 0.00089, 0.089, 0.000089, 0.0089, 0.000089]

def get_numberReads(file, fastq=True): # returns number of reads in sample
    with open(file, "r") as f:
        lines = f.read().split("\n")
        if fastq:
            return len(lines)/4
        else:
            return len(lines)/2

def get_numberReadsSample(sample): # predefined values to save time
    size = {'gridion364': 3491390, 'gridion366':3667480, 'promethion365':35810963, 'promethion367':34573282}
    return size[sample]

def get_sequences(file, fastq=True): #returns read sequences of samples
    with open(file, "r") as f:
        fast = f.read().split("\n")
        if fastq:
            seq = fast[1:len(fast):4]
        else:
            seq =fast[1:len(fast):2]
    return seq

def get_averageSeqLength(file, fastq=True, median=True): #returns either median or arith. mean seq length
    seq = get_sequences(file, fastq)
    lengths = [len(x) for x in seq]
    if median:        
        return int(np.median(lengths))
    else:
        return int(round(np.sum(lengths)/len(lengths), 0))

def get_sampleName(file): #return name of sample
    file = file.split("/")[-1]
    return file.split("_")[0]

def get_MedianLengthOfBestMatch(classification): # for kaiju, returns median match length
    with open(classification, 'r') as f:
        lines = f.readlines()
        matchLengths=[]
        for line in lines:
            line = line.split("\t")
            if line[0]=="C":
                matchLengths.append(int(line[3]))
    return int(np.median(matchLengths))

def get_groundTruth(report): # ground truth vector based on species level for all species
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
    return data

def get_abundances(report): #returns abundances for classifis species
    prediction=[]
    
    with open(report, 'r') as report:
        lines = report.readlines()
        for line in lines:
            line = line.split("\t")
            if "S" == line[2]:
                prediction.append(float(line[0]))
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




