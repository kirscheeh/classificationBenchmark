#!/bin/bash

input="files"
CONDA=$(which conda)

while read -r line; do
  if [[ "$line" == \#* ]]; then
    echo "# Last Update:" $(date)
  elif [[ ! "$line" == "" ]]; then
    IFS=' ' read -r -a array <<< "$line"
    $CONDA env export --name ${array[0]} > ${array[1]} &> echo && echo "$CONDA env export --name ${array[0]} > ${array[1]}" || echo "Building ${array[1]} failed. For Error Message, see above."
    
  fi
done < "$input" > current.md

mc current.md README.md
