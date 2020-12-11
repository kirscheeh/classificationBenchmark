#!/bin/bash
# This scripts exports the used conda environments into yaml-files

input="../envs/README.md"
CONDA=$(which conda)

while read -r line; do
  if [[ "$line" == \#* ]]; then
    echo "# Last Update:" $(date)
  elif [[ ! "$line" == "" ]]; then
    IFS=' ' read -r -a array <<< "$line"
    $CONDA env export --name ${array[0]} > ../envs/${array[1]} && echo "${array[0]} ${array[1]}" || echo "Building ${array[1]} failed."
  fi
done < "$input" > ../envs/current.md

mv ../envs/current.md ../envs/README.md