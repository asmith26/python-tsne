#!/bin/bash

file=$1
echo "Running $file"
# cat $file | sed "s:\]:\n:g" | wc -l
sed -i "s:\]::g" $file
# cat $file | sed "s:\[::g" | wc -l
sed -i "s:\[::g" $file
sed -i "s:\,::g" $file

# wc -l $file
# cat $file | while read line; do echo $line | wc -w; done

