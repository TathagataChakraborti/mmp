#/usr/bin/env bash

# path to pr2plan #
#PR2PLAN_PATH=$(locate pr2plan | head -n 1)

# ground domain and problem input using pr2plan #
python3 ./grounder/grounder_interface.py $1  $2 Test $3
