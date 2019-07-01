from pylab import *

# colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']


colors = ['r','b']

zmax=2.5
a = linspace(1,1/(1+zmax),30)
z = 1/a-1

#zz = array([0.0125, 0.0384, 0.0656, 0.0943, 0.1247, 0.1567, 0.1906, 0.2266, 0.2648, 0.3055,
# 0.3488, 0.3952, 0.4448, 0.4982, 0.5556, 0.6175, 0.6846, 0.7576, 0.8371, 0.9242,
# 1.0199, 1.1257, 1.2431, 1.3743, 1.5217, 1.6887, 1.8794, 2.0992, 2.3554, 2.5])

w = loadtxt('EOS_full.txt')
wd = loadtxt('EOS_ref_0523_x2.txt')

fig = figure(figsize=(6,4))

ax = fig.add_subplot(1,1,1)


#############################################################################################
#ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[0],label=r'JD16',alpha=0.3)
#ax.plot(z,w[:,0],ls='-',lw=2,color=colors[0],alpha=0.75)
#ax.plot(z,w[:,2],ls='-',lw=1,color=colors[0],alpha=0.75)
#ax.plot(z,w[:,3],ls='-',lw=1,color=colors[0],alpha=0.75)

#ax.errorbar(z,wd[:,0],yerr=[wd[:,0]-wd[:,2],wd[:,3]-wd[:,0]],label=r'JD16$\ast$',fmt='s-',ms=5,capsize=3,capthick=2,color=colors[1],alpha=0.75)

#############################################################################################
ax.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[0],label=r'JD16',alpha=0.3)
ax.plot(z,w[:,0],ls='-',lw=2,color=colors[0],alpha=0.75)
ax.plot(z,w[:,0]-w[:,1],ls='-',lw=1,color=colors[0],alpha=0.75)
ax.plot(z,w[:,0]+w[:,1],ls='-',lw=1,color=colors[0],alpha=0.75)
#ax.plot(z,w[:,2],ls=':',lw=1,color=colors[0],alpha=0.5)
#ax.plot(z,w[:,3],ls=':',lw=1,color=colors[0],alpha=0.5)

ax.errorbar(z,wd[:,0],yerr=wd[:,1],label=r'JD16$^{\ast}$',fmt='s-',ms=5,capsize=3,capthick=2,color=colors[1],alpha=0.75)
#ax.plot(z,wd[:,2],ls='--',lw=1,color=colors[1],alpha=0.5)
#ax.plot(z,wd[:,3],ls='--',lw=1,color=colors[1],alpha=0.5)

ax.hlines(-1,xmin=0.0,xmax=zmax,linestyle='dashed',color='k',lw=2,alpha=0.5)

ax.set_xlim(0,zmax)
xticks = [0,0.5,1.0,1.5,2.0,2.5]
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

savefig('w_results_2016.pdf')
#savefig('w_results_2016_two_tails.pdf')

show()
