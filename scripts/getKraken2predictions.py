import sys, os

species = ['Bacillus subtilis', 'Listeria monocytogenes', 'Enterococcus faecalis', 'Staphylococcus aureus', 'Salmonella enterica', 'Escherichia coli', 'Pseudomonas aeruginosa', 'Lactobacillus fermentum', 'Saccharomyces cerevisiae', 'Cryptococcus neoformans']
predictions = {}
total=0
if len(sys.argv) == 2:
    for s in species:
        os.system('grep -n "{spec}" {file} > helping.log'.format(spec=s, file=sys.argv[1]))
        with open('helping.log', 'r') as report:
                perc = float(report.readline().split("\t")[0].split(": ")[1])
                total+=perc
        predictions[s] = perc

predictions['unclassified']=100-total
print(predictions)
os.system('rm helping.log')
