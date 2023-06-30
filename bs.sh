#!/bin/bash
for i in {1..50}
do
	python3 bs.py $i
	#pkill python3
done
