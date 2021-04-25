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

counter_headers=0
old_name=""
counter=1
old_taxid=""
#headers=open(sys.argv[1], 'r')
while True:
    header = sp.getoutput('grep -m 1 "\[" '+sys.argv[1])
        
    if not header:
        exit()

    name = getName(header)
    header = header.split(" ")[0]
    print(header)
    if name==old_name:
        counter+=1
    else:
        old_name=name
        counter = 1
        taxid = species2TaxID(name)
    os.system("sed -i 's/{}.*/>".format(header)+str(counter)+"_"+str(taxid)+"/' "+sys.argv[1])
    counter_headers+=1

    if counter_headers % 100 ==0:
        print("Another thousand done")
   # 
  #  os.system("sed -i 's/"+str(headerStart)+".*/>"+str(species[1])+"_"+str(taxid)+"/' "+str(sys.argv[2]))
    #if counter==100:
     #   print("100 Done")
      #  counter=0

#try:
#        species[name]+=1
#    except KeyError:
#        species[name]=0