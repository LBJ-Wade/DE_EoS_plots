
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

fig = plt.figure(figsize=(7,4.5))

ax = plt.gca()

eos_SP1 = np.loadtxt('eos_SP_6a.txt')
eos_SP2 = np.loadtxt('eos_SP_6ai.txt')

a = np.linspace(1,.4,20)
z = 1/a-1

colors=['k','r','b']
ax.hlines(-1,xmin=0,xmax=1.5,linestyle='dashed',lw=2.5,alpha=1,color=colors[0])

ax.fill_between(z,y1=eos_SP1[:,1], y2=eos_SP1[:,2], color=colors[1], alpha=0.65, label=r'Original reuslt')
ax.plot(z,eos_SP1[:,0],'--',color=colors[1])

ax.fill_between(z,y1=eos_SP2[:,1], y2=eos_SP2[:,2], color=colors[2], alpha=0.65, label=r'Error signs inverted')
ax.plot(z,eos_SP2[:,0],'--',color=colors[2])

ax.set_xlim(-0.01,1.51)
ax.set_ylim(-3.5,0.5)

ax.set_xticks([0,0.5,1.0,1.5])
ax.set_xticklabels([0,0.5,1.0,1.5],fontsize=13)
ax.set_yticks([-3,-2,-1,0])
ax.set_yticklabels([-3,-2,-1,0],fontsize=13)

ax.set_xlabel(r'$z$',fontsize=14)
ax.set_ylabel(r'$w(z)$',fontsize=14)
lgd=ax.legend(loc='lower left',frameon=False,fontsize=13)
ax.tick_params(axis='both',direction='in')

texts = lgd.get_texts()
cid=[1,2]
for i in range(len(texts)):
	plt.setp(texts[i],color=colors[cid[i]],fontsize=13)

plt.savefig('w_vs_err.pdf')
plt.show()
