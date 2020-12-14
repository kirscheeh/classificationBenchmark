#!/bin/bash
# This scripts exports the used conda environments into yaml-files

INPUT="../envs/README.md"
CURRENT="../envs/current.md"
CONDA=$(which conda)

while read -r line; do
  if [[ "$line" == \#* ]]; then
    echo "# Last Update:" $(date)
  elif [[ ! "$line" == "" ]]; then
    IFS=' ' read -r -a array <<< "$line"
    $CONDA env export --name ${array[0]} > ${array[1]} && echo "${array[0]} ${array[1]}" || echo "Building ${array[1]} failed."
  fi
done < "$INPUT" > "$CURRENT"

mv *.yml ../envs/
mv "$CURRENT" "$INPUT"

function whatthehell() {
  echo "what am i doing here?"
  if [[ $1 -ge 9000 ]]; then
    echo "level of boredom:" $1
  fi
} 