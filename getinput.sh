#!/bin/bash
day="day$(printf %02d $1)"
aoc_path="${BASH_SOURCE[0]%/*}"

if [[ -z "$1" ]]; then
    echo "Add a day number argument (don't need 0 padding)"
    exit 1
fi
if [[ ! -d "$aoc_path/$day" ]]; then
    echo "Make a directory for that day first"
    exit 1
fi

wget "https://adventofcode.com/2021/day/$1/input" \
    -P "$aoc_path/$day" \
    --header="cookie: $(cat $aoc_path/cookie)"
