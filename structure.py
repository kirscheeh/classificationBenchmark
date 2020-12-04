#!/usr/bin/python3

""" 
PROJECT WORK -- Benchmarking several classification tools regarding their usability for long reads

This script creates the structure of folders used in this project for reproducibility. The user has to declare destinations for databases and results.

@Kirsten, 02.12.2020
"""
# absolute paths!
#DATABASE="/your/path/to/location/database"
RESULTS="/your/place/to/location/results" # optionally, this is the parent folder of this git repository

#####################################################################################

import os

# in the future: incoorportate a separate file where the user can gather the used tools
tools = ["kaiju", "kraken2", "centrifuge", "taxmaps", "kslam", "deepmicrobes", "clark", "ccmetagen", "metaothello", "nbc", "megablast"]

def generate_folders(path):
    if os.path.exists(path):
        print("This folder already exists!", path)
    else:
        os.mkdir(path)
        for tool in tools:
            print(tool)
            os.mkdir(path+"/"+tool)

generate_folders(RESULTS)







