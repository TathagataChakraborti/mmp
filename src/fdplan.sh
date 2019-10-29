#/usr/bin/env bash

# path to fast downward #
FD_PATH=$(locate fast-downward.py | head -n 1)

# find optimal plan using fd on input domain and problem #
rm -f output output.sas sas_plan 
${FD_PATH} $1 $2 --search "astar(lmcut())" > /dev/null 2>&1
if [ $? -eq 3 ]
then
    rm -f output output.sas sas_plan 
    ${FD_PATH} $1 $2 --search "astar(hmax())" | grep -e \([0-9]\) | awk '{$NF=""; print $0}'
else
    cat sas_plan|grep -v ";"| sed 's/(//'| sed 's/)//' 
    #| awk '{$NF=""; print $0}'
fi
