#!/usr/bin/env bash
set -e

HISTTIMEFORMAT="%F %T "
err() {
    echo "========== error"
    # history 10 | head -n -1
    history 10
    echo "Error occurred:"
    awk 'NR>L-4 && NR<L+4 { printf "%-5d%3s%s\n",NR,(NR==L?">>>":""),$0 }' L=$1 $0
}
trap 'err $LINENO' ERR

set -o history
set -x
true
uname
for i in 1 2 3 4 5
do
    echo $i
done
echo 1
echo 1
echo 1
echo 1
echo 1


echo one
echo two
false
echo five
echo six

history


set +o history
history -cw
fping free.fr
df

history


