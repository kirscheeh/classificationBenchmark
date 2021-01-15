# script for calculatig abundance similarity profiles
# IDAS
#- this calculation can also be manually performed by reweighting the read counts after classification
#- To generate the abundance profile vector, each individual species sum is divided by the total abundance classified at a given taxonomic rank - either species or genus
#- calculate pairwise distance between the species abundance profiles for each classification method

# need to known how the output of the different tools looks like
# use getKraken2proportions.py
#1. real abundance vector
#2. observed abundance vector
#3. L2 distance between vectors
#4. repeat for all datasets
