import sys, os

species = ['Bacillus subtilis  ', 'Listeria monocytogenes  ', 'Enterococcus faecalis  ', 'Staphylococcus aureus  ', 'Salmonella enterica  ', 'Escherichia coli  ', 'Pseudomonas aeruginosa  ', 'Lactobacillus fermentum  ', 'Saccharomyces cerevisiae  ', 'Cryptococcus neoformans  ']
preditcions = {}
if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as report:
        for s in species:
            preditcions[s] = os.system('grep -n "{species}" file'.format(species=s, file=sys.argv[1]))

print(preditcions)