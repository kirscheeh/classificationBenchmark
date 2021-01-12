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


# l2 norm of a vector
from numpy import array
from numpy.linalg import norm
a = array([17.51, 12.87, 11.11, 11.07, 5.69, 5.25, 4.48, 14.14, 2.18, 2.0, 9.13]) #kraken2 testing output
a =a/100
b = array([12,12,12,12,12,12,12,12,2,2,0])
b=b/100
c=b-a
l2 = norm(c)
print(l2)