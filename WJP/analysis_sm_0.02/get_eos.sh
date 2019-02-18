#!/bin/bash

n=46

while [ $n -le 46 ]
do
awk 'NR==8, NR==27' results/EoS_$n.margestats | \
awk '{ print $2,$3,$4,$5,$7,$8}' > EoS/eos_$n.txt
n=`expr 1 + $n`
done
