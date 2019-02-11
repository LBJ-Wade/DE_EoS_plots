
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
# colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']
colors = [u'b', u'r', u'g', u'#d62728', u'#9467bd', u'#8c564b']

###########################################################

fig = plt.figure(figsize=(6,4))

alpha = 1

###########################################################
# eigen spectrum of data and prior
###########################################################

ax = plt.gca()

covmat_data = np.loadtxt('EoS_jla_wmap9_cov.txt')
prior_smoothed = np.loadtxt('CPZ_prior_smoothed_ac_0.06_sigma_mw_0.04_inv.txt')

val_data,vec_data = eig(covmat_data)
val_p1,vec_p1 = eig(prior_smoothed)

val_data = np.real(val_data)
val_p1 = np.real(val_p1)

idx_data = np.argsort(val_data)
idx_p1 = np.argsort(val_p1)

val_data = val_data[idx_data]
val_p1 = abs(val_p1[idx_p1])

x = np.arange(1,21)

ax.plot(x,np.log10(val_p1),'-.s',ms=4,label=r'Continuity prior ($\sigma_{\bar{w}}=0.04, a_s=0.06$)', color=colors[0], alpha=alpha)
ax.plot(x,np.log10(1/val_data),':o',markersize=4,label=r'Mock data (JLA + WMAP9)', color=colors[1], alpha=alpha)

ax.set_xticks([0,5,10,15,20])
ax.set_xlabel(r'Eigenmode number',fontsize=12)

ax.set_ylim(-3.5,6)
ax.set_ylabel(r'$\log_{10}\left[1/\sigma^{2}\right]$',fontsize=12)
lgd = ax.legend(loc='best',frameon=False,fontsize=11)
ax.tick_params(axis='both',direction='in')

# get legend handles and then set the colors for the legend texts (and some extra texts)
lines = lgd.legendHandles
texts = lgd.get_texts()

for i in range(len(lines)):
	plt.setp(texts[i],color=colors[i],fontsize=12)

plt.savefig('eigen_spectrum.pdf')
plt.show()
