#!/bin/bash
#set -x

#exec 2> >(grep -v "Killed by signal 1.")

ssh_tunnel_send() 
{
    local route=$1
    local dest=$2

    local fname=${3:-NONE}

    echo "tar zcf - $fname  |  ssh   -J  ${route} ${dest}  'tar xzf - ' "
    tar zcf - $fname  |  ssh   -J  ${route} ${dest}  'tar xzf - ' 
}

ssh_tunnel_recv() 
{
    local route=$1
    local dest=$2

    local fname=${3:-NONE}

    ssh  -J  ${route} ${dest}  "tar zcf - $fname"  | tar xzf -
}

_test_ssh_tunnel_sendrecv()
{
    cat <<-EOF > tmp_test
    THIS IS TEST FILE 
EOF
    local sha=$(sha1sum tmp_test)

    ssh_tunnel_send mppa-server011,hudson@192.168.122.70 root@10.3.0.1  tmp_test
    rm -f tmp_test
    ssh_tunnel_recv mppa-server011,hudson@192.168.122.70 root@10.3.0.1  tmp_test

    [ "$sha" == "$(sha1sum tmp_test)" ] && echo TEST_PASSED && return
    echo "TEST FAILED"}
}

# example of use
# bash ssh_tunnel_send.sh  mppa-server011,hudson@192.168.122.70 root@10.3.0.1  <file_to_send>

