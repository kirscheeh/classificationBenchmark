#!/bin/bash

input="../envs/test.ms"

while IFS= read -r line
do
  if [[ "$line" == \#* ]]; then
    echo "# Last Update:" $(date)
  else
    "$line"
    echo "$line"
  fi
done < "$input" > current.md 
