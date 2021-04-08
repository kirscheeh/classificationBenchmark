#!/usr/bin/python3

""" 
PROJECT -- Benchmarking several classification tools regarding their usability for long reads

This script creates the structure of folders used in this project for reproducibility. The user has to declare destinations for databases and results.

@Kirsten, 02.12.2020
"""

#####################################################################################

import os, yaml

config = open("config.yaml", "r")
parsed_yaml = yaml.load(config)
classification_tools = parsed_yaml['classification']
path=parsed_yaml['path']
classification_path=path+"/result/classification"

def generate_folder(path, folders=[]):
    if os.path.exists(path):
        print("This folder already exists!", path)
    else:
        print(path)
        try:
            os.mkdir(path)
        except FileNotFoundError:
            os.makedirs(path)
    
    if len(folders)>0:
        for folder in folders:
            generate_folder(path+"/"+folder)

generate_folder(path)
generate_folder(classification_path, classification_tools)
