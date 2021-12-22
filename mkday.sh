#!/bin/bash
day="day$(printf %02d $1)"
if [[ -d "$day" ]]; then
    echo "A directory for that day already exists"
    exit 1
fi

cp -r "template" "$day"
mv "$day/template.py" "$day/$day.py"
./getinput.sh $1

echo "created $day"
