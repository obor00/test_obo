#!/bin/bash
set -x

exec 2> >(grep -v "Killed by signal 1.")

ssh_propagate() 
{
    local first_route=$1; shift
    local list_intermediate_ip="$@"
    local ipddr

    ssh-copy-id "$first_route"

    route="$first_route"
    for ipaddr in $list_intermediate_ip
    do
        next_hop=$1; shift
        cat  ~/.ssh/id_rsa.pub |  ssh   -J  ${route} ${next_hop}  'cat >  ~/.ssh/authorized_keys' 
        route+=",${next_hop}"
    done
}

# example of use
# ssh_propagate.sh mppa-server011 hudson@192.168.122.70  root@10.3.0.1
ssh_propagate $@

