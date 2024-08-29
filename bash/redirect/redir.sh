#!/bin/bash

set -x 

echo "p out"
echo "p err" >&2

exec &> >(tee toto) 2>&1

echo "p2 out"
echo "p2 err" >&2
ls
