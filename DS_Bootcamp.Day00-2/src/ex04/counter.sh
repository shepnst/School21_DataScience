#!/bin/sh

INPUT='../ex03/hh_positions.csv'
OUTPUT='hh_uniq_positions.csv'

if [ -f "$INPUT" ]; then
    echo '"name"', '"count"' > "$OUTPUT"
    cat "$INPUT" | tail -n 20 | cut -d',' -f3 | sort | uniq -c | sort -n -r | awk '{print $2 ", " $1}' | sed 's/^ *//' >> "$OUTPUT"
    echo "output is done"

else
    echo "the initial .csv file doesnt exist"
fi
