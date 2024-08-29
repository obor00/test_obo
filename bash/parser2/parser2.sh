#!/bin/bash
declare -A boot_status

ff()
{
    readarray -t lines < rauc
    for key in $(seq 1 ${#lines[@]})
    do
        local entries=( ${lines[$key]} )
        #echo $entries
        [[ ${entries[0]} == "Activated:" ]] && boot_activated=${entries[1]}
        [[ ${entries[0]} == "x" ]] || [[ ${entries[0]} == "o" ]] && \
            tmptxt="${entries[1]/[/}" &&  boot_section="${tmptxt/]/}"
        [[ ${entries[0]} == "boot" ]] && [[ ${entries[1]} == "status:" ]] && \
            boot_status[$boot_section]=${entries[2]}
    done

    echo "boot_activated=$boot_activated"

    for key in ${!boot_status[@]} ; do
        echo "key=$key"
        echo "status=${boot_status[$key]}"
    done
}

ff
