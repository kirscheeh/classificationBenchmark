#!/bin/bash
# script for splitting the promethion input and proecssing it in pices --> not used
head -12000000 "$1" > "$2" 
kma -i "$1" -t_db "$3" -o helper -t 8 -1t1 -mem_mode -and -ef
cat helper >> "$4".res
for i in {1..12} 
do
    start=$((12000000*i))
    end=$((start+12000000))
    sed -e "1,${start}d;${end}q" $1 > $2
    kma -i "$2" -t_db "$3" -o helper.$i -t 8 -1t1 -mem_mode -and -ef
    cat helper >> "$4".res
done
rm helper
cat *mapstat* >> "$4".mapstat