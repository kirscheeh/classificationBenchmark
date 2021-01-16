#!/usr/bin/env python

"""
This script returns the seed length a classifier should use regarding the median length of the input reads and considering the percentage the seed should make up for of this length.

@Kirsten, 12/2020
"""
# tools to use it: centrifuge, kaiju?
# TODO
# - File einlesen
# - Durchschnittliche Readlänge berechnen --> vllt. wegen der Laufzeit nur jeden 2. Read angucken?
#   - Vielleicht nicht Durchschnitt, sondern Median? Kann durch die durchschnittliche Länge nicht unclassified bleiben?
# - Ausrechnen
# - Kann ich das auch für jeden Read machen? Fallen dann ggf. nicht viele Reads raus?
#   - Jeder Read geht nicht, weil centrifuge bspw. ein ganzes File nimmt und classified
#   - Tool für jeden Read einzeln aufrufen? Ergibt das Sinn?

