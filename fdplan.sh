#/usr/bin/env bash

# path to fast downward #
FD_PATH="/home/ASUAD/tchakra2/Desktop/FAST-DOWNWARD/fast-downward.py"

# find optimal plan using fd on input domain and problem #
rm -f output output.sas sas_plan
${FD_PATH} $1 $2 --search "astar(lmcut())" | grep -e \([0-9]\) | awk '{$NF=""; print $0}'
