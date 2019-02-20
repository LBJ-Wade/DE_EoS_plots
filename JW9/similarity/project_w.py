from pylab import *

eos = loadtxt('EoS.old/eos_3.txt')

vecs  = loadtxt('JLA_WMAP9_SP_vecs.txt')

alpha_w = []
alpha_1w = []

w = eos[:,0]

for i in range(20):
	alpha_w.append(matmul(w,vecs[i,:]))
	alpha_1w.append(matmul(w+1,vecs[i,:]))

# add w=-1 projection result
# w_tmp = -1*ones(20)
# alpha_w.append(matmul(w+1,w_tmp))
# alpha_1w.append(matmul(w+1,w_tmp))

plot(alpha_w,'r-o',label='projection onto w(z)')
plot(alpha_1w,'b-s',label='projection onto 1+w(z)')


legend(loc='best',frameon=False)

show()