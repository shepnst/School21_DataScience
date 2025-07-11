
#!/bin/sh

INPUT='../ex01/hh.csv'
OUTPUT='hh_sorted.csv'

if [ -f "$INPUT" ]; then
    cat "$INPUT" | head -n 1 > "$OUTPUT"
    cat "$INPUT" | tail -n 20 | sort -t ',' -k 2 -k 1 >> "$OUTPUT"
    echo "csv is edited"

else
    echo "the initial .csv file doesnt exist"

fi