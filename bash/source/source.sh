#!/bin/bash

[ $# -ne 1 ] && echo "Error" &&  return

echo "sourcing $@"
echo "sourcing 0=$0"
echo "sourcing 1=$1"

source source2.sh
