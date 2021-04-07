#!/bin/bash
# helper script to combine Python and R script for extracting and visualizing Precision and Recall

if [ "$#" -eq 2 ]; then
    python scripts/extractingVal4Vis.py $1 scripts/helper.tsv # getting the ground truth and abundance
    Rscript scripts/visPRCurve.R helper.tsv $2 $1 # plotting PR Curve and getting AUPR
    rm scripts/helper.tsv
else
    echo "Missing arguments."
    echo "Usage: PRCurve.sh AREPORT NEW-PNG"
fi
