#!/bin/bash
# script for automating the calculating of abundance profile similarities

cd scripts
python abundanceProfileSimilarity.py "$1" "$2" >> "$3"
cd ..
