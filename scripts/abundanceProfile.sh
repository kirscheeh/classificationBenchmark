#!/bin/bash
# script for automating the calculating of abundance profile similarities

cd scripts
python -c"import getting; getting.get_APS(\"$1\","$2", printing=True)" #>> /mnt/fass1/kirsten/result/classificationBenchmark/this_is_a_test.txt
cd ..
