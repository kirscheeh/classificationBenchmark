#!/usr/bin/python3

""" 
PROJECT WORK -- Benchmarking several classification tools regarding their usability for long reads

This script creates the structure of folders used in this project for reproducibility. The user has to declare destinations for databases and results.

@Kirsten, 02.12.2020
"""

#####################################################################################

import os

config = open("config.yaml", "r").read()
variables = config.split('\n')

# filter comments and empty entries
variables = [x for x in variables if not "#" in x and not '' == x]
# get path to main folder
for x in variables:
    if "path" in x:
        path = x.split("[")[1][:-1]
        classification_path=path+"/classification"
    if "classification" in x:
        classification_tools = x.split("{")[1][:-1].split(", ")

def generate_folder(path, folders=[]):
    if os.path.exists(path):
        print("This folder already exists!", path)
    else:
        print(path)
        os.mkdir(path)
    
    if len(folders)>0:
        for folder in folders:
            generate_folder(path+"/"+folder)

generate_folder(path)
generate_folder(classification_path, classification_tools)
