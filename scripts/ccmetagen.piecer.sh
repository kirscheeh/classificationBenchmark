#!/bin/bash
# script for splitting the promethion input

start="$2"
end="$3"
sed -e "1,${start}d;${end}q" $1 > $2

#head -12000000 "$1" > "$2" 
#for i in {1..15} #12
#do
#    start=$((12000000*i))
#    end=$((start+12000000))
#    sed -e "1,${start}d;${end}q" $1 > $2
#done