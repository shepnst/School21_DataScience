#!/bin/sh

INPUT='../ex02/hh_sorted.csv'
OUTPUT='hh_positions.csv'

if [ -f "$INPUT" ]; then
    {
        head -n 1 "$INPUT"
        tail -n 20 "$INPUT" | awk -F, '{
            name=$3;
            position="";
            if (name ~ /(Junior|Middle|Senior)/){ #if name contains something from "Junior|Middle|Senior"
                if (name ~ /Junior/){
                    position=position "Junior/";
                }
                if (name ~ /Middle/){
                    position=position "Middle/";
                }
                if (name ~ /Senior/){
                    position=position "Senior/";
                }
                sub(/\/$/, "", position); #delete the last charachter is exists
            }
            else{
                position="-";
            }
            print $1 "," $2 ",\"" position "\"," $4 "," $5;
        }'
    } > "$OUTPUT"
    echo "csv is edited"

else
    echo "the initial .csv file doesnt exist"

fi