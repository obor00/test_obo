#!/bin/bash
set -x
callFuncs() {
    # Set up indirect references as positional parameters to minimize local name collisions.
    set -- "${@:1:3}" ${2+'a["$1"]' "$1"'["$2"]'}

    # The only way to test for set but null parameters is unfortunately to test each individually.
    local x
    for x; do
        [[ $x ]] || return 0
    done

    local -A a=(
        [foo]='([r]=f [s]=g [t]=h)'
        [bar]='([u]=i [v]=j [w]=k)'
        [baz]='([x]=l [y]=m [z]=n)'
        ) ${4+${a["$1"]+"${1}=${!3}"}} # For example, if "$1" is "bar" then define a new array: bar=([u]=i [v]=j [w]=k)

        echo ${4+${a["$1"]+"${1}=${!3}"}} # For example, if "$1" is "bar" then define a new array: bar=([u]=i [v]=j [w]=k)

    ${4+${a["$1"]+"${!4-:}"}} # Now just lookup the new array. for inputs: "bar" "v", the function named "j" will be called, which prints "j" to stdout.
}

main() {
    # Define functions named {f..n} which just print their own names.
    local fun='() { echo "$FUNCNAME"; }'

    for x in {f..n}; do
        eval "${x}${fun}"
    done

    callFuncs "$@"
}

main "$@"

