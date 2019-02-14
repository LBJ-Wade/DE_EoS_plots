import sys,os
import numpy as np
import matplotlib.pylab as plt
from scipy.linalg import eig

colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']
ls = ['-','--',':','-.']
lw = 2

lgd_size=12

###########################################################
# plot EoS synthesized from PCs and alphas
def w_fun(alphas=None,alpha_errs=None,vecs=None,max_idx=20):
	w = np.zeros(20)-1.
	werr = np.zeros(w.shape)
	for i in range(max_idx):
		w += alphas[i]*vecs[i,:]
		werr += (alpha_errs[i]*vecs[i,:])**2

	return w, werr**0.5

# max_idx = [1,2,3,4]
max_idx = [2,4,6]
###########################################################
fig = plt.figure(figsize=(6,6))
text_x,text_y = 0.5,0.9
ymax=0.95
hlw=0.6

a = np.linspace(1,0.4,20)
z = 1.0/a - 1.0


###########################################################
# B-1) best PCs from data + (marg-) prior
plt.subplot(2,1,1)
ax = plt.gca()

vecs = np.loadtxt('Data_SP_vecs.txt')
vals = np.loadtxt('Data_SP_vals.txt')

ax.plot(z,vecs[0,:],'-', lw=lw,label=r'WPC1 ('+str(round(np.real(vals[0]),2))+')')
ax.plot(z,vecs[1,:],'--',lw=lw,label=r'WPC2 ('+str(round(np.real(vals[1]),2))+')')
ax.plot(z,vecs[2,:],':', lw=lw,label=r'WPC3 ('+str(round(np.real(vals[2]),2))+')')
ax.plot(z,vecs[3,:],'-.',lw=lw,label=r'WPC4 ('+str(round(np.real(vals[3]),2))+')')

ax.set_xlim(-0.025,1.525)
ax.set_xticklabels([])
ax.set_ylim(-1*ymax,ymax)
ax.set_xlabel(r'$z$',fontsize=14)
ax.set_ylabel(r'${\bf e}_i(z)$',fontsize=14)

ticks = [0,0.25,0.5,0.75,1.0,1.25,1.5]
ticklabels = []
for i in range(len(ticks)): ticklabels.append(str(ticks[i]))
ax.set_xticks(ticks)
# ax.set_xticklabels(ticklabels,fontsize=14)

ticks = [-0.5,0,0.5]
ticklabels = []
for i in range(len(ticks)): ticklabels.append(str(ticks[i]))
ax.set_yticks(ticks)
ax.set_yticklabels(ticklabels,fontsize=12)

ax.tick_params(axis='both',direction='in')
ax.hlines(0,xmin=0,xmax=1.5,linestyle='dashed',lw=hlw,alpha=0.65)

lgd=ax.legend(loc='upper center',ncol=2,frameon=False,fontsize=lgd_size)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],color=colors[i])


###########################################################
plt.subplot(2,1,2)
ax = plt.gca()

# load full EoS recontruction result: Data + SP
# eos_SP = np.loadtxt('eos_SP.txt')
eos_SP = np.loadtxt('eos_SP_6a.txt')

dz=0
max_idx = 4

    
alpha = np.loadtxt('alpha_SP.txt')
vecs = np.loadtxt('Data_SP_vecs.txt')
w,werr=w_fun(alpha[:,0],alpha[:,1],vecs,max_idx=max_idx)

ax.fill_between(z,y1=eos_SP[:,1],y2=eos_SP[:,2],label='Original result',color='r',alpha=0.5)
ax.errorbar(z+dz,w,yerr=werr,capsize=4,capthick=2,elinewidth=2,color='b',marker='D',markersize=4,label='Synthesized from WPC1-4')
ax.set_xlim(-0.025,1.525)
ax.set_ylim(-3.5,0)
ax.set_xlabel(r'$z$',fontsize=14)
ax.set_ylabel(r'$w(z)$',fontsize=14)

ticks = [0,0.5,1.0,1.5]
ticklabels = []
for i in range(len(ticks)): ticklabels.append(str(ticks[i]))
ax.set_xticks(ticks)
ax.set_xticklabels(ticklabels,fontsize=13)

ticks = [-3,-2,-1,-0]
ticklabels = []
for i in range(len(ticks)): ticklabels.append(str(ticks[i]))
ax.set_yticks(ticks)
ax.set_yticklabels(ticklabels,fontsize=13)

ax.hlines(-1,xmin=0,xmax=1.5,linestyle='dashed',lw=hlw,alpha=0.5)

lgd=ax.legend(loc='lower left',ncol=1,frameon=False,fontsize=lgd_size)
texts = lgd.get_texts()
plt.setp(texts[0],color='r')
plt.setp(texts[1],color='b')


###########################################################
plt.subplots_adjust(wspace=0.175,
                    # hspace=0.225,
                    hspace=0.0,
                    left=0.15,
                    right=0.95,
                    top=0.975,
                    bottom=0.1)

plt.savefig('synthesis_EoS_v3.pdf')
plt.show()
