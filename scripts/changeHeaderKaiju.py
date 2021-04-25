# this scripts changes the faa output headers accordingly to Kaiju regulatory: >prefix_taxID
# first arg: list with headers, second arg: faa file
import sys, os
from ete3 import NCBITaxa
import subprocess as sp

def species2TaxID(species):
    return NCBITaxa().get_name_translator([species])[str(species)][0]

def getName(line):
    name = line.split("\n")[0].split("[")[1][:-1]
    return name

counter=0
headers = open(sys.argv[1], 'r')
old_name=""
old_taxid=0
counter_headers=0
for header in headers:
    try:
        name = getName(header)
        if old_name==name:
            counter+=1
        else:
            old_name=name
            counter=1
            taxid=species2TaxID(name)
        headerStart=header.split(" ")[0]
        os.system("sed -i 's/"+str(headerStart)+".*/>"+str(counter)+"_"+str(taxid)+"/' "+str(sys.argv[2]))
        counter_headers+=1
        if counter_headers % 100 == 0:
            print(counter_headers)
    except Exception:
        pass
