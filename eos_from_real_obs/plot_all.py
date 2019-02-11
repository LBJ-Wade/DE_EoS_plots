from pylab import *

zmax = 1.5
amin = 1./(1.+zmax)
a = linspace(1,amin,20)
z = 1/a-1.

eos = [
'plk2015_snls3_bao_hz_h0_a_2.0_sm_0.04.txt',
'wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt',
'wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt_0',
# 'wmap9dp_jla_bao_hz_a_2.0_sm_0.02_0.04.txt',
# 'wmap9dp_jla_bao_hz_h0_a_2.0_sm_0.02.txt',
'wmap9dp_jla_bao_hz_h0_a_2.0_sm_0.04.txt',
# 'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.02.txt',
'wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt',
# 'wmap9dp_snls3_bao_hz_h0_a_2.0_sm_0.08.txt',
# 'wmap9dp_union_bao_h0_hz_a_2.0_sm_0.02.txt',
'wmap9dp_union_bao_h0_hz_a_2.0_sm_0.04.txt',
# 'wmap9dp_union_bao_hz_h0_a_2.0_sm_0.02.txt',
# 'wmap9dp_union_bao_hz_h0_a_2.0_sm_0.04.txt'
]

for i in range(len(eos)):
	w = loadtxt(eos[i])
	plot(z,w[:,0],label=eos[i])

legend(loc='best',frameon=False)

show()