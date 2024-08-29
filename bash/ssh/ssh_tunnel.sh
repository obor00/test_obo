#!/bin/bash
#set -x

#exec 2> >(grep -v "Killed by signal 1.")

ssh_tunnel() {
    local tunnel=$1;  shift
    local dest=$1;  shift
    ssh -J $tunnel $dest  "$@"
}

ssh_tunnel_nofail() {
    local tunnel=$1;  shift
    local dest=$1;  shift
    ssh -J $tunnel $dest  "$@"
    return 0;
}

# Example of use

#route="mppa-server011,hudson@192.168.122.70"
#dest="root@10.3.0.1"
#ssh_tunnel $route $dest myscript.sh
#echo "result=$?"



