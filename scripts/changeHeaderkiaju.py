# this scripts changes the faa output headers accordingly to Kaiju regulatory: >prefix_taxID
# first arg: list with headers, second arg: faa file
import sys, os
from ete3 import NCBITaxa

def species2TaxID(species):
    return NCBITaxa().get_name_translator([species])[str(species)][0]

def getName(line):
    name = line.split("\n")[0].split("[")[1][:-1]
    return name

headers=open(sys.argv[1], 'r')

species={}
for header in headers:
    name = getName(header)
    taxid = species2TaxID(name)

    headerStart=header.split(" ")[0]
    try:
        species[name]+=1
    except KeyError:
        species[name]=0
    os.system("sed -i 's/"+str(headerStart)+".*/>"+str(species[name])+"_"+str(taxid)+"/' "+str(sys.argv[2]))
