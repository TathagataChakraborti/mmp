#/usr/bin/env bash

# path to pr2plan #
#PR2PLAN_PATH=$(locate pr2plan | head -n 1)

# ground domain and problem input using pr2plan #
rm -f *-domain.pddl *-problem.pddl obs.dat
cp $1 tr-domain.pddl
cp $2 tr-problem.pddl
