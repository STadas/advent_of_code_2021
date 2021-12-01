#!/bin/bash
if [[ -d "day$1" ]]; then
    echo "a directory for that day already exists!"
else
    cp -r "template" "day$1"
    mv "day$1/template.py" "day$1/day$1.py"

    echo "created day$1"
fi
