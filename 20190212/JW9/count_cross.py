from pylab import *

# EoS_dir = 'EoS.inv_err'

tot_size = 1000

EoS_dir = 'EoS.ref'


def count_cross(eos_result):
	cnt1,cnt2 = 0,0

	w = loadtxt(eos_result)
	w_m = w[:,0]
	w_std = w[:,1]
	w_low = w[:,2]
	w_up  = w[:,3]

	sign1 = 0 # number of {w_i} less than -1
	sign2 = 0 # number of {w_i} greater than -1

	# sign1 = sum((w_m+1)/w_std<-1)
	# sign2 = sum((w_m+1)/w_std>1)
	sign1 = sum((w_m+1)<0)
	sign2 = sum((w_m+1)>0)

	if abs(sign1) >= 1 and abs(sign2) >= 1:
		return 1
	else:
		return 0


cnt = []
for i in range(1,tot_size):
	eos_result = EoS_dir+'/eos_'+str(i)+'.txt'
	cnt.append(count_cross(eos_result))

print(sum(cnt))