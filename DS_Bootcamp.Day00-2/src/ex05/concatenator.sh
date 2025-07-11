#!/bin/sh

OUTPUT="result.csv"
if ls *.csv 1> /dev/null 2>&1; then
    HEADER=$(head -n 1 $(ls *.csv | head -n 1))
    echo "$HEADER" > "$OUTPUT"
    first_file=$(ls *.csv | head -n 1)
    for file in *.csv; do
        if [ "$file" = "$first_file" ]; then
            tail -n +2 "$file" >> "$OUTPUT"
        elif [ "$file" != "$OUTPUT" ]; then
            tail -n +2 "$file" >> "$OUTPUT"
        fi
    done
    echo "complete"
else
    echo "error"
fi