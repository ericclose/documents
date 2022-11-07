#!/bin/bash

# with cidr notation
ip addr show scope global | grep -w inet | awk '{ printf $2 "\n" }'

# without cidr notation
ip addr show scope global | grep -w inet | awk '{ printf $2 }' | awk -F '/' '{ printf $1 "\n" }'

exit 0
