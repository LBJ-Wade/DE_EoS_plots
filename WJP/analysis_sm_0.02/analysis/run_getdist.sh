#!/bin/bash

n=46

Nmax=46


while [ $n -le $Nmax ]
do
FILE_ROOT="../EoS_SN_CMB"
m4 	-DKEY_FILE_ROOT="file_root = $FILE_ROOT" \
	-DKEY_OUT_ROOT="out_root = ./results/EoS_$n" \
	"GetDist.ini" > "dist.ini"

# run GetDist
getdist "dist.ini"
#rm "dist.ini"
n=`expr $n + 1`
#sleep 2
done
