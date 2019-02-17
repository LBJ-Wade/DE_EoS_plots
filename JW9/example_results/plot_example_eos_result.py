
###########################################################
# 2019-02-07: 删除了marginalized prior
#
###########################################################

import sys,os
import numpy as np
import matplotlib.pylab as plt
from scipy.linalg import eig
from scipy.stats import norm, kstest, normaltest

# use default colors defined by MatPlotlib
colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']

###########################################################

fig = plt.figure(figsize=(11,4))

###########################################################
# 1) histograms of the normalized dmu(zi). The purpose is
# to show that the mock sample is not too peculiar
###########################################################

def read_snls3_mock( mock_filename ):
	fp = open(mock_filename,'r')
	lines = fp.readlines()
	fp.close()

	snls3 = []
	for line in lines:
		sn = line.split()
		temp = []
		temp.append(float(sn[1]))
		temp.append(float(sn[2]))
		temp.append(float(sn[3]))
		temp.append(float(sn[4]))
		snls3.append(temp)

	return np.array(snls3)

# snls3 = read_snls3_mock('MOCK_JLA_1.txt')
snls3 = read_snls3_mock('MOCK_JLA_6a.txt')
# snls3 = read_snls3_mock('MOCK_JLA_5a.txt')
z = snls3[:,0]
dmu = (snls3[:,1]-snls3[:,3])/snls3[:,2] # normalize the errors
# dmu = (snls3[:,1]-snls3[:,3])

nbin_all = 15
nbin_1 = 15
nbin_2 = 15
z1 = 0.2
z2 = 0.6
ID1 = (z <  z1 )
ID2 = (z >= z2 )

p  = round(kstest(dmu,cdf='norm')[1],2)
p1 = round(kstest(dmu[ID1],'norm')[1],2)
p2 = round(kstest(dmu[ID2],'norm')[1],2)

plt.subplot(1,2,1)
ax = plt.gca()

rwidth=0.6
ax.hist(dmu, bins=nbin_all, label=r'ALL', alpha=0.5, rwidth=rwidth, color=colors[0])
ax.hist(dmu[ID1], bins=nbin_1, label=r'$z<' + str(z1) + '$', alpha=0.7, rwidth=rwidth, color=colors[1])
ax.hist(dmu[ID2], bins=nbin_2, label=r'$z\geq' + str(z2) + '$', alpha=0.8, rwidth=rwidth, color=colors[2])

# add p-vale
ax.text(0.175,0.5,r'p = '+str(p),
		color=colors[0],
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes,
        fontsize=14)

ax.set_xlim(-3.5,3.5)
ax.set_xticks([-3,-2,-1,0,1,2,3])
ax.set_xticklabels([-3,-2,-1,0,1,2,3],fontsize=14)
ax.set_xlabel(r'$\widetilde{\Delta\mu}$',fontsize=14)

ax.set_yticks([0,20,40,60,80,100,120,140])
ax.set_yticklabels([0,20,40,60,80,100,120,140],fontsize=14)
ax.set_ylabel(r'Counts',fontsize=14)

ax.tick_params(axis='both',direction='in')

lgd=ax.legend(loc='upper left',fontsize=14,frameon=False)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],color=colors[i])

###########################################################
# 3) reconstructed EoS
###########################################################
plt.subplot(1,2,2)
ax = plt.gca()

# loadtxt reconstruction results (obtained using GetDist)
# eos_SP = np.loadtxt('eos_SP.txt')
eos_SP = np.loadtxt('eos_SP_6a.txt')

a = np.linspace(1,.4,20)
z = 1/a-1

colors=['blue','red']
ax.hlines(-1,xmin=0,xmax=1.5,linestyle='dashed',lw=2,alpha=1,color=colors[0],label=r'Fiducal model')
ax.errorbar(z,eos_SP[:,0],yerr=[eos_SP[:,0]-eos_SP[:,1],eos_SP[:,2]-eos_SP[:,0]],
			marker='o',elinewidth=1.5,markersize=4,capsize=3,capthick=2,color=colors[1],label=r'Reconstruction')

ax.set_xlim(-0.025,1.525)
ax.set_xticks([0,0.25,0.5,0.75,1.0,1.25,1.5])
ax.set_xticklabels([0,0.25,0.5,0.75,1.0,1.25,1.5],fontsize=14)
ax.set_xlabel(r'$z$',fontsize=14)

ax.set_yticks([-3,-2.5,-2,-1.5,-1,-0.5])
ax.set_yticklabels([-3,-2.5,-2,-1.5,-1,0.5],fontsize=14)
ax.set_ylabel(r'$w(z)$',fontsize=14)
lgd=ax.legend(loc='lower left',frameon=False,fontsize=14)
ax.tick_params(axis='both',direction='in')

texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],color=colors[i])

###########################################################
# final adjustments ...
plt.subplots_adjust(wspace=0.2,
                    hspace=0.25,
                    left=0.065,
                    right=0.985,
                    top=0.975,
                    bottom=0.175)

plt.savefig('example_eos_result.pdf')
plt.show()
