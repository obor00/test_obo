#!/bin/bash

myv="p1 p2 p3"

myf()
{
    echo "now executing  $*"
    $*
    cat
}

cat << EOF | myf
hello2 
EOF

cat << EOF | ssh 127.0.0.1
echo "KKKKK  myv=$myv" 
list="\$(ls -m tmp)"
list="\${list/,/ }"

for i in \$list
do
    echo "==> $myv , \$i"
done
EOF

