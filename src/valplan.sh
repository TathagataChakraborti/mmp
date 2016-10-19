#/usr/bin/env bash

# path to fast downward #
VAL_PATH=$(locate VAL/validate)

# validate plan given domain and problem
output=$(${VAL_PATH} $1 $2 $3 | grep "Successful plans:")
if [[ "Successful plans:" == ${output} ]]; then
    echo "True"
else
    echo "False"
fi
