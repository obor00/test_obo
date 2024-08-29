#!/bin/bash
set -x

runRemote() {
    local dest=$1;  shift
    local script=$1; shift
    local args
    printf -v args '%q ' "$@"
    ssh $dest  "bash -s" <<EOF

    # pass quoted arguments through for parsing by remote bash
    set -- $args

    # substitute literal script text into heredoc
    $(< "$script")

EOF
}

runRemote2() {
    local dest=$1;  shift
    local script=$1; shift
    local args

    # generate eval-safe quoted version of current argument list
    printf -v args '%q ' "$@"

    # pass that through on the command line to bash -s
    # note that $args is parsed remotely by /bin/sh, not by bash!
    ssh user@remote-addr "bash -s -- $args" < "$script"
}

runRemote  $@
#runRemote  mppa-server011 run_remote.sh  hudson@192.168.122.70  ./remote_script.sh  "param1" "param2"



