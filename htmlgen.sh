#!/bin/bash
for i in {1..50}
do
    python3 htmlgen.py $i
    pkill firefox
    pkill python3
done
