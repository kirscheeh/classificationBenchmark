import sys, os

def getProportions(f):
        species = ['Bacillus subtilis', 'Listeria monocytogenes', 'Enterococcus faecalis', 'Staphylococcus aureus', 'Salmonella enterica', 'Escherichia coli', 'Pseudomonas aeruginosa', 'Lactobacillus fermentum', 'Saccharomyces cerevisiae', 'Cryptococcus neoformans', 'unclassified']
        predictions = {}
        #total=0

        for s in species:
                os.system('grep -n "{spec}" {file} > helping.log'.format(spec=s, file=f))
                with open('helping.log', 'r') as report:
                        line = report.readline()
                        
                        if not '\tS\t' in line and not '\tU\t' in line:
                                test=report.readline()
                                perc = float(test.split("\t")[0].split(": ")[1])
                                print(test)
                        else:
                                print(line)
                                perc = float(line.split("\t")[0].split(": ")[1])
                        #total+=perc
                predictions[s] = perc
        os.system('rm helping.log')
        print(predictions.values())
        return list(predictions.values())


if len(sys.argv) == 2:
        getProportions(sys.argv[1])
