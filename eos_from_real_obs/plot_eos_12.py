from pylab import *

# colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']

colors = ['r','b']

a = linspace(1,0.4,20)
z = 1/a-1

# w = loadtxt('wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt')
# wd = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt')

# updated reconstruction results
w = loadtxt('eos_WMAP9_SNLS3_HZ_BAO_H0.txt')
wd = loadtxt('eos_fiducial.txt')

dz = 0.00

fig = figure(figsize=(6,4))

ax = fig.add_subplot(111)

# ax.errorbar(z+dz,w[:,0],yerr=[w[:,0]-w[:,2],w[:,3]-w[:,0]],
# 	marker='s',markersize=5,capsize=4,capthick=2,color=colors[1],
# 	label=r'SNLS3+BAO+H(z)+WMAP9')

ax.errorbar(z-dz,wd[:,0],yerr=[wd[:,0]-wd[:,2],wd[:,3]-wd[:,0]],
	marker='o',markersize=5,capsize=4,capthick=2,color=colors[1],
	label=r'JD12$\ast$')


ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[0],label=r'JD12',alpha=0.3)
ax.plot(z,w[:,0],ls='-',lw=2,color=colors[0],alpha=0.75)
ax.plot(z,w[:,2],ls='-',lw=1,color=colors[0],alpha=0.75)
ax.plot(z,w[:,3],ls='-',lw=1,color=colors[0],alpha=0.75)

# ax.fill_between(z,y1=wd[:,2],y2=wd[:,3],color=colors[1],label=r'SNLS3+BAO+H(z)+WMAP9 distance prior',alpha=0.3)

# ax.plot(z,wd[:,0],ls='--',lw=2,color=colors[1],label=r'SNLS3+BAO+H(z)+WMAP9 distance prior',alpha=0.75)
# ax.plot(z,wd[:,2],ls='--',lw=1,color=colors[1],alpha=0.75)
# ax.plot(z,wd[:,3],ls='--',lw=1,color=colors[1],alpha=0.75)

ax.hlines(-1,xmin=0.0,xmax=1.6,linestyle='dashed',color='k',lw=2,alpha=0.5)

ax.set_xlim(0,1.5)
xticks = [0,0.5,1.0,1.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)
ax.set_xlabel(r'$z$',fontsize=13)

ax.set_ylim(-2.05,0.05)
yticks = [-2,-1.5,-1,-0.5,0]
ax.set_yticks(yticks)
ax.set_ylabel(r'$w(z)$',fontsize=13)
ax.set_yticklabels(yticks,fontsize=13)

ax.tick_params(axis='both',direction='in')

lgd=legend(loc='best',frameon=False,fontsize=13)
texts = lgd.get_texts()
plt.setp(texts[0],fontsize=14,color=colors[0])
plt.setp(texts[1],fontsize=14,color=colors[1])

fig.subplots_adjust(top=0.995,bottom=0.125,left=0.125,right=0.975)

savefig('w_results_2012.pdf')

show()
