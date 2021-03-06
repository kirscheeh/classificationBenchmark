# Script with several useful functions  needed across the different scripts
import os, yaml
import numpy as np
config='../config.yaml'
from numpy import array
from numpy.linalg import norm

def get_species(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            species = parsed_yaml['species']
        return species
    else:
        print('Error! No config file', config)

def get_path(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            path = parsed_yaml['path']
        return path[0]
    else:
        print('Error! No config file', config)

def get_dataIndices(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            index = parsed_yaml['dataIndex']
        return index
    else:
        print('Error! No config file', config)

def get_samples(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            samples = parsed_yaml['samples']
            return samples
    else:
        print('Error! No config file', config)

def get_number_species(areport):
    number=0
    with open(areport, "r") as report:
        lines = report.readlines()
        print(len(lines))
        for line in lines:
            if line.split("\t")[2] == "S":
                number+=1
    return number

def get_tools_classification(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            tools = parsed_yaml['classification']
        return tools
    else:
        print('Error! No config file', config)

"""def get_abundances(tool, report, config):
    predictions={}
    species = get_species(config)
    #total=0
    for s in species:
        os.system('grep -n "{spec}" {file} > helping.log'.format(spec=s, file=report))
        with open('helping.log', 'r') as f:
            line = f.readline()
            if tool in ['kraken2', 'centrifuge']:
                if not '\tS\t' in line and not '\tU\t' in line:
                        test=f.readline()
                        perc = float(test.split("\t")[0].split(": ")[1])
                else:
                        perc = float(line.split("\t")[0].split(": ")[1])
                #total+=perc/100
                predictions[s] = perc/100
    os.system('rm helping.log')
    #print(total)
    print(predictions.values())
    return predictions"""

def get_abundances(areport, config):
    predictions={}
    species = get_species(config)
    #total=0
    for s in species:
        os.system('grep -n "{spec}" {file} > helping.log'.format(spec=s, file=areport))
        os.system('grep -n "{spec}" {file}'.format(spec=s, file=areport))
        with open('helping.log', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split("\t")
                if line[4][:-1] == s and line[2]=="S":
                    predictions[s] = float(line[0].split(":")[1])
                else:
                    predictions[s] = 0
            if (len(lines)) == 0:
                predictions[s] = 0

    os.system('rm helping.log')
    #print(total)
    print(list(predictions.values()))
    return predictions

get_abundances("../stats/gridion364_default.clark.areport", "../config.yaml")

def get_ASP(areport, truth):
    predi = get_abundances(areport, config).values()
    pred=list(predi)
    print(pred)
    try:
        t = np.array(truth)
        p = np.array(pred)
        print(max(p))
        l2 = np.sum(np.power((t-p),2))
        return l2
    except Exception as e:
        print("An error occured.", e)


def get_numberReads(file, fastq=True):
    with open(file, "r") as f:
        lines = f.read().split("\n")
        if fastq:
            return len(lines)/4
        else:
            return len(lines)/2

def get_sequences(file, fastq=True): #fastq is boolean
    with open(file, "r") as f:
        fast = f.read().split("\n")
        if fastq:
            seq = fast[1:len(fast):4]
        else:
            seq =fast[1:len(fast):2]
    return seq

def get_qualityStrings(file):
    with open(file, "r") as f:
        fast = f.read().split("\n")
    return fast[3:len(fast):4]

def get_seqLength(file, fastq=True, median=True): 
    seq = get_sequences(file, fastq)
    lengths = [len(x) for x in seq]
    if median:        
        return int(np.median(lengths))
    else:

        return int(round(np.sum(lengths)/len(lengths), 0))

def get_quality(file, median): #phred64, might be really slow
    qualSeq = get_qualityStrings(file)
    qual = []
    asciiValues = {chr(i):i-64 for i in range(64, 106)}#{chr(i):i-33 for i in range(33, 76)} # ascii mapped to Q-value
    for seq in qualSeq:
        current=0
        for c in seq:
            current+=asciiValues[c]
        qual.append(current)
    if median:
        return np.median(qual)
    else:
        return int(round(np.sum(qual)/len(qual), 0))

def get_qualityFast(file, ignoreSeq, ignoreChar, median): #ignoreX is int, gives number of characters and sequences that should be ignored to fasten up the process
    qualSeq = get_qualityStrings(file)
    asciiValues = {chr(i):i-64 for i in range(64, 106)}
    qual=[]
    for i in range(0, len(qualSeq), ignoreSeq):
        current=0
        for j in range(0, len(qualSeq[i]), ignoreChar):
            try:
                current+=asciiValues[qualSeq[i][j]]
            except IndexError:
                pass
        qual.append(current)
    if median:
        return np.median(qual)
    else:
        return round(qual/len(qual), 0)








