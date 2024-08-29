#!/bin/bash

echo $0 $1 $*
show()
{
    echo show
    echo $ENVV
}


test()
{
    echo "string"
echo ${FUNCNAME[0]}
}


echo $BASH_SOURCE
echo $BASH_LINENO

echo ${FUNCNAME[*]}


echo "$1"
for cmd in "$@"
do
"$cmd"
done
