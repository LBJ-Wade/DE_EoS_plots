from pylab import *

ct = loadtxt('cross_times.txt')

fp1 = open('../3x3_examples/ids_good.txt','w')
fp2 = open('../3x3_examples/ids_1sigma.txt','w')
fp3 = open('../3x3_examples/ids_2sigma.txt','w')

i = 0
while i < 100:
	if ct[i,0] <= 0 and ct[i,1] <= 0:
		fp1.write('%5d\n'%(i+1))
	elif ct[i,0] > 0 and ct[i,1] <= 0:
		fp2.write('%5d\n'%(i+1))
	elif ct[i,1] > 0:
		fp3.write('%5d\n'%(i+1))

	i += 1

fp1.close()
fp2.close()
fp3.close()