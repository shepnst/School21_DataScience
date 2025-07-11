#!/bin/sh


INPUT='../ex00/hh.json'
if [ -f "$INPUT" ]; then
    jq -r -f filter.jq "$INPUT" > hh.csv
    echo "csv is edited"

else
    echo "the .json file doesnt exist"

fi