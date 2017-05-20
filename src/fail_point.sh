# path to fast downward #
VAL_PATH=$(locate VAL/validate|head -n 1)

# validate plan given domain and problem
output=$(${VAL_PATH} -v $1 $2 $3 |grep time|tail -n 1|awk '{print $NF}'|sed 's/)//')
echo ${output} 

