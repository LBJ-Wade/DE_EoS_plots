import os, sys
from pylab import *

# EoS_dir = 'EoS.inv_err'

NUM=-1
EoS_dir = None

if len(sys.argv) < 3:
    print('usage: %s EoS_dir result_num'%(sys.argv[0]))
    sys.exit(0)
else:
    EoS_dir = sys.argv[1]
    NUM = int(sys.argv[2])

T1_1sigma = []
T1_2sigma = []
T2_1sigma = []
T2_2sigma = []

for i in range(1,NUM+1):
	w = loadtxt(EoS_dir+'/eos_'+str(i)+'.txt')
	T1_1sigma.append(sum( abs((w[:,0]+1)/w[:,1]) >= 1 ))
	T1_2sigma.append(sum( abs((w[:,0]+1)/w[:,1]) >= 2 ))

	n1 = 0
	n2 = 0
	for j in range(len(w[:,0])):
		if (w[j,0] > -1) and (w[j,2] > -1):
			n1 += 1

		if (w[j,0] < -1) and (w[j,3] < -1):
			n1 += 1

		if (w[j,0] > -1) and (w[j,4] > -1):
			n2 += 1

		if (w[j,0] < -1) and (w[j,5] < -1):
			n2 += 1

	# print('%3d wi deviates from w=-1 more than 1-sigma!'%(n))
	T2_1sigma.append(n1)
	T2_2sigma.append(n2)

T1_1sigma = array(T1_1sigma)
T1_2sigma = array(T1_2sigma)
T2_1sigma = array(T2_1sigma)
T2_2sigma = array(T2_2sigma)


print('--> 1 sigma level:')
print(sum(T1_1sigma>0))
print(sum(T2_1sigma>0))

print('--> 2 sigma level:')
print(sum(T1_2sigma>0))
print(sum(T2_2sigma>0))
