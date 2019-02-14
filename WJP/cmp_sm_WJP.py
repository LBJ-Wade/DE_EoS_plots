import sys
from pylab import *

zmax=1.7
amin=1/(1+zmax)
a = linspace(1,amin,20)
z = 1/a-1

colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']

fig = figure(figsize=(7,4.5))

cid=[2,0,1]

ids = [46]
cnt=1

dz=0.005

ax = fig.gca()

w = loadtxt('EoS_sm_0.02/eos_'+str(ids[cnt-1])+'.txt')
ax.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],label=r'$\sigma_{\bar{w}}=0.02$',color=colors[cid[0]],alpha=0.5)

w = loadtxt('EoS_sm_0.04/eos_'+str(ids[cnt-1])+'.txt')
ax.errorbar(z-dz,w[:,0],yerr=w[:,1],fmt='d-.',ms=5,capsize=3,capthick=3,label=r'$\sigma_{\bar{w}}=0.04$',color=colors[cid[1]])

w = loadtxt('EoS_sm_0.08/eos_'+str(ids[cnt-1])+'.txt')
ax.errorbar(z+dz,w[:,0],yerr=w[:,1],fmt='v--',ms=5,capsize=3,capthick=3,label=r'$\sigma_{\bar{w}}=0.08$',color=colors[cid[2]])


ax.hlines(-1,xmin=0,xmax=1.7,linestyles='dashed',color='grey',linewidth=1)

ax.set_xlim(0-5*dz,1.7+5*dz)
ax.set_ylim(-2.5,0)
ax.set_xticks([0,0.5,1.0,1.5])
ax.set_xticklabels([0,0.5,1.0,1.5],fontsize=13)
ax.set_yticks([-2.5,-2,-1.5,-1,-0.5,0])
ax.set_yticklabels([-2.5,-2,-1.5,-1,-0.5,0],fontsize=13)

ax.set_xlabel('z',fontsize=13)
ax.set_ylabel(r'$w(z)$',fontsize=13)

lgd=ax.legend(loc='lower left',frameon=False,fontsize=13)
texts = lgd.get_texts()
for i in range(len(texts)):
    plt.setp(texts[i],fontsize=13,color=colors[cid[i]])

ax.text(0.6,-2.25,'WFIRST + JLA + Planck',fontsize=14,color='k')

fig.savefig('WJP_cmp_sigma_w.pdf')

show()
