#!/bin/bash
#set -x

exec 2> >(grep -v "Killed by signal 1.")

ssh_tunnel() {
    local tunnel=$1;  shift
    local dest=$1;  shift
    local script=$1; shift
    local args
    printf -v args '%q ' "$@"
    ssh -J $tunnel $dest  "bash -s" <<EOF

    # pass quoted arguments through for parsing by remote bash
    set -- $args

    # substitute literal script text into heredoc
    $(< "$script")

EOF
}

cat <<- EOF > myscript.sh
  uname -a
  echo "titi" > toto
  # cmd_does_not_exist
EOF


# Example of use

route="mppa-server011,hudson@192.168.122.70"
dest="root@10.3.0.1"
ssh_tunnel $route $dest myscript.sh
echo "result=$?"



