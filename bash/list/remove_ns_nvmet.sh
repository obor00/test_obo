#!/bin/bash

ns_to_del=$(find ./dir1  -name device_path | xargs grep $1)

for i in $ns_to_del
do
    name=${i//:*/}
    echo $name
    echo ${name//device_path/}
done


