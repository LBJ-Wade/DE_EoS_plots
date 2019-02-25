
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

fig = plt.figure(figsize=(7,4))

alpha = 1

###########################################################
# eigen spectrum of data and prior
###########################################################

ax = plt.gca()

prior_smoothed = np.loadtxt('CPZ_prior_smoothed_ac_0.06_sigma_mw_0.04_inv.txt')

val_p,vec_p = eig(prior_smoothed)
val_p = np.real(val_p)
idx_p = np.argsort(val_p)
val_p = abs(val_p[idx_p])

x = np.arange(1,21)

# ax.plot(x,np.log10(val_p),'-.s',ms=4,label=r'Continuity prior ($\sigma_{\bar{w}}=0.04, a_s=0.06$)', color=colors[0], alpha=alpha)
ax.plot(x,val_p,':s',ms=4,label=r'$\sigma_{\bar{w}}=0.04, a_c=0.06$', color=colors[0], alpha=alpha)

xticks=[0,5,10,15,20]
ax.set_xticks(xticks)
ax.set_xlabel(r'Eigenmode number',fontsize=12)

# ax.set_ylim(-3.5,6)
# ax.set_ylabel(r'$\log_{10}\left[1/\sigma^{2}\right]$',fontsize=12)
ax.set_ylabel(r'Eigen values ($\lambda_i$)',fontsize=12)

lgd = ax.legend(loc='best',frameon=False,fontsize=11)
ax.tick_params(axis='both',direction='in')

# get legend handles and then set the colors for the legend texts (and some extra texts)
texts = lgd.get_texts()

for i in range(len(texts)):
	plt.setp(texts[i],color=colors[i],fontsize=12)


l0,b0 = 0.2,0.65
w,h = 0.2,0.175

dl = w*1.1
db = h*1

a = np.linspace(1,.4,20)
z = 1/a-1

cnt = 1
for i in range(3):
	for j in range(2):
		rect = [l0+j*dl,b0-i*db,w,h]
		ax=fig.add_axes(rect)
		ax.plot(z,vec_p[:,idx_p[cnt-1]],'-')
		ax.set_ylim(-0.65,.85)
		ax.text(0.1,0.4,r'$\sqrt{\lambda_'+str(cnt)+'} = $ '+str(round(val_p[cnt-1],3)),color='r')
		# ax.legend(loc='upper left',frameon=False,markerscale=0)
		if i==2:
			ax.set_xlabel('z')
			ax.set_xticks([0,0.5,1,1.5])
		else:
			ax.set_xticks([])
		if j==1:
			ax.set_yticks([])
		else:
			ax.set_yticks([-0.5,0,0.5])

		ax.tick_params(axis='both',direction='in')
		cnt += 1

fig.subplots_adjust(top=0.995,right=0.975)

plt.savefig('prior_eigen_spectrum.pdf')

plt.show()
