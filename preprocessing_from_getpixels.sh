#!/bin/bash

# cat pixels_X.txt | sed "s:\]:\n:g" | wc -l
sed -i "s:\]:\n:g" pixels_X.txt
# cat pixels_X.txt | sed "s:\[::g" | wc -l
sed -i "s:\[::g" pixels_X.txt
sed -i "s:\,::g" pixels_X.txt

# wc -l pixels_X.txt
# cat pixels_X.txt | while read line; do echo $line | wc -w; done
