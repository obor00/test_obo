#!/bin/bash

declare -A t


for i in ta tb tc
do
    for j in key1 key2 key3
    do
        t[$i$j]="hello $i$j"

    done
done


echo ${t[@]}

for i in ta tb tc
do
    for j in key1 key2 key3
    do
        echo ${t[$i$j]} 

    done
done



