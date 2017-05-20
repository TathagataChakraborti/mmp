#/usr/bin/env bash

cat sas_plan |grep "\; cost ="|awk '{print $4}'
rm sas_plan
