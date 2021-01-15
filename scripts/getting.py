# Script with several useful functions  needed across the different scripts
import os, yaml
from numpy import array
from numpy.linalg import norm
config='../config.yaml'

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

def get_tools_classification(config):
    if os.path.isfile(config):
        with open(config, 'r') as c:
            parsed_yaml = yaml.load(c)
            tools = parsed_yaml['classification']
        return tools
    else:
        print('Error! No config file', config)

def get_abundances(tool, report, config):
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
    return predictions

get_abundances('kraken2', '../report/gridion_ERR3152364_test.kraken2.report', config)

def get_ASP(tool, report, truth):
    pred = get_abundances(tool, report, config)
    try:
        result=norm(truth-pred)
        print(result)
        return result
    except Exception:
        print("An error occured.")

