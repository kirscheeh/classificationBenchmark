#!/bin/bash
# script for automating the calculating of abundance profile similarities

python -c"import getting; getting.get_APS(\""$1\"", $2, printing=True)" >> $3