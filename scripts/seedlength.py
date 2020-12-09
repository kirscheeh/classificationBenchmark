#!/usr/bin/env python

"""
This script calculates a desired seed length given a file containing reads and the percentage that the seed should make up to the average length of the reads.
"""

# TODO
# - File einlesen
# - Durchschnittliche Readlänge berechnen --> vllt. wegen der Laufzeit nur jeden 2. Read angucken?
#   - Vielleicht nicht Durchschnitt, sondern Median? Kann durch die durchschnittliche Länge nicht unclassified bleiben?
# - Ausrechnen
# - Kann ich das auch für jeden Read machen? Fallen dann ggf. nicht viele Reads raus?
#   - Jeder Read geht nicht, weil centrifuge bspw. ein ganzes File nimmt und classified
#   - Tool für jeden Read einzeln aufrufen? Ergibt das Sinn?

import sys, statistics, math

def getAverage(seq):
    lengths = [len(x) for x in seq]
    return math.ceil(statistics.median(lengths)*float(sys.argv[2])) #always rounding up

if len(sys.argv) != 4:
    print("Wrong number of arguments.")
    print("Usage: seedlength.py FASTA PERC INT")
    print("Where FASTA is a path to a fasta or fastq file and PERC (0-1) denominated the percentage of the median read length the seed should have. INT specifies the number of reads that should be considered (1: everyone, 2: every second, 3: every third, ....")
else:
    with open(sys.argv[1], "r") as file:
        fast = file.read().split("\n")
        if fast[2][0] == "+": # check if fastq
            avg = getAverage(fast[1:len(fast):4*int(sys.argv[3])])
        else:
            avg = getAverage(fast[1:len(fast):2*int(sys.argv[3])])

