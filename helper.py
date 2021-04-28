with open('help', 'r') as f:
    counter=0
    for line in f:
        counter+=float(line)

print(counter/4)