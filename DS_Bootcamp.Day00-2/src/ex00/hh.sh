#!/bin/sh

VACANCY=$1   
OUTPUT='hh.json'
URL='https://api.hh.ru/vacancies'

if [ $# -eq 1 ]; then
    curl -s -H  'User-Agent: sc21_test' -G "$URL" --data-urlencode "text=$VACANCY" --data-urlencode "per_page=20" \
    --data-urlencode "page=0" | jq > "$OUTPUT"
    echo "json is edited"

else
    echo "you should pass the argument."
fi