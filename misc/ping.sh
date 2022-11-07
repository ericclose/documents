#!/bin/bash

## 批量 ping 脚本 demo

IP_PREFIX="209.141.61."

myping() {
    ping -c4 $1 &>/dev/null
    if [ "$?" -eq 0 ]; then
        echo "$1 is up."
    else
        echo "$1 is down."
    fi
}

for IP_SUFFIX in {1..254}; do
    myping "$IP_PREFIX""$IP_SUFFIX" &
done

exit 0
