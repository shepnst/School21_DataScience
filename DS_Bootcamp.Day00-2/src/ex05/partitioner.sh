#!/bin/sh

INPUT='../ex03/hh_positions.csv'
HEADER=$(head -n 1 "$INPUT")

if [ -f "$INPUT" ]; then
    awk -F, -v header="$HEADER" 'BEGIN{
    }
    NR==1{
        next;
    }
    {
        split($2, datetime, "T");
        date = datetime[1];

        gsub(/"/, "", date);
        gsub(/ /, "_", date);
    
        if (!(date in files)) {
            files[date] = 1;
            print header > (date ".csv");
        }
        print $0 >> (date ".csv");
    }
    ' "$INPUT"
    echo "complete"

else
    echo "the initial .csv file doesn't exist"
fi
