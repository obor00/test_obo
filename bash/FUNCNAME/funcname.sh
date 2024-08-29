#!/bin/bash

f1()
{
    echo "here f1"
    i=0
    while [[ -n "${FUNCNAME[$i]}" ]] ; do
        echo ${FUNCNAME[$i]} ${BASH_SOURCE[$i]}  ${BASH_LINENO[$i]}
        i=$((i+1))
    done
}

f2()
{
    echo "here f2"
    f1
}

f2
