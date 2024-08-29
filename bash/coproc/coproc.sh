#!/bin/bash

coproc FDS { ./fils.sh ; }
echo "it is me" >&${FDS[1]}
read -ru ${FDS[0]} foo
echo $foo

