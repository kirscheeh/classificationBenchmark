#!/bin/bash
# helper script to combine Python and R script for extracting and visualizing Precision and Recall
# has to be called from classificationBenchmark

if [ "$#" -eq 3 ]; then
    python scripts/extractingVal4Vis.py $1 scripts/helper.tsv # getting the ground truth and abundance
    Rscript scripts/visPRCurve.R $3 helper.tsv $2 $1 # plotting PR Curve and getting AUPR
    rm scripts/helper.tsv
else
    echo "Missing arguments."
    echo "Usage: PRCurve.sh AREPORT NEW-JPEG PATH/TO/classificationBenchmark/scripts"
    echo "The output file needs an absolute path."
    echo "You have to call this script from /PATH/TO/classificationBenchmark."
fi
