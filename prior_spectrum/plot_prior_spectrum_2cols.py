
###########################################################
# 2019-02-07: 删除了marginalized prior
#
###########################################################

import sys,os
import numpy as np
import matplotlib.pylab as plt
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from scipy.linalg import eig
from scipy.stats import norm, kstest, normaltest

# use default colors defined by MatPlotlib
# colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']
colors = [u'b', u'r', u'g', u'#d62728', u'#9467bd', u'#8c564b']

###########################################################

fig = plt.figure(figsize=(10,4))

alpha = 1

###########################################################
# eigen spectrum of data and prior
###########################################################

#ax = plt.gca()
ax = fig.add_axes([0.085,0.125,0.415,0.865])
patches = []

prior_smoothed = np.loadtxt('CPZ_prior_smoothed_ac_0.06_sigma_mw_0.04_inv.txt')

val_p,vec_p = eig(prior_smoothed)
val_p = np.real(val_p)
idx_p = np.argsort(val_p)
val_p = abs(val_p[idx_p])

x = np.arange(1,21)

ax.plot(x,val_p,':s',ms=4, color=colors[0], alpha=alpha)

xticks=[0,5,10,15,20]
ax.set_xticks(xticks)
ax.set_xlabel(r'Eigenmode number',fontsize=12)

ax.set_ylabel(r'Eigen values ($\lambda_i$)',fontsize=12)

lgd = ax.legend(loc='best',frameon=False,fontsize=11)
ax.tick_params(axis='both',direction='in')

#ax.set_yticks([5000,10000,15000,20000])
#ax.set_yticklabels([r'$5\times 10^3$',r'$1\times 10^4$',r'$1.5\times 10^4$',r'$2\times 10^4$'])

# get legend handles and then set the colors for the legend texts (and some extra texts)
texts = lgd.get_texts()

for i in range(len(texts)):
	plt.setp(texts[i],color=colors[i],fontsize=12)

ellipse_loc = [4.5,5]
ellipse = mpatches.Ellipse(ellipse_loc,8,2300)
patches.append(ellipse)

dx = 4.5
dy = 5500
arrow = mpatches.Arrow(4.5, 1500, dx, dy,width=2.5)
patches.append(arrow)

colors = np.linspace(0, 1, len(patches))
collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
ax.add_collection(collection)


# add inset in the left panel
rect = [0.135,0.45,0.25,0.5]
ax=fig.add_axes(rect)
ax.plot(x[0:8],val_p[0:8],':s',ms=4, color='b', alpha=alpha)
#ax.set_ylim(-0.65,.65)
ax.set_yticks([0,15,30,45])


### NOW plot subplots in the right panel

l0,b0 = 0.55,0.70
w,h = 0.215,0.288

dl = w*1.025
db = h*1

a = np.linspace(1,.4,20)
z = 1/a-1

cnt = 1
for i in range(3):
	for j in range(2):
		rect = [l0+j*dl,b0-i*db,w,h]
		ax=fig.add_axes(rect)
		ax.plot(z,vec_p[:,idx_p[cnt-1]],'b-')
		ax.set_ylim(-0.65,.65)
		if abs(val_p[cnt-1]) < 1e-5:
		    ax.text(0.1,0.35,r'$\lambda_'+str(cnt)+' = $ '+str(0),color='r',fontsize=13)
		else:
		    ax.text(0.1,0.35,r'$\lambda_'+str(cnt)+' = $ '+str(round(val_p[cnt-1],3)),color='r',fontsize=13)
		if i==2:
			ax.set_xlabel('$z$')
			ax.set_xticks([0,0.5,1,1.5])
		else:
			ax.set_xticks([])
		if j==1:
			ax.set_yticks([])
		else:
			ax.set_yticks([-0.5,0,0.5])

		ax.tick_params(axis='both',direction='in')
		cnt += 1


plt.savefig('prior_eigen_spectrum.pdf')

plt.show()
