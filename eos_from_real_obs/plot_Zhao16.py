from pylab import *

colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']

zmax=2.5
a = linspace(1,1/(1+zmax),30)
z = 1/a-1

w = loadtxt('eos_PLK15_JLA_DR12BAO_Hz_HST.txt')


fig = figure(figsize=(6,7))

ax = fig.add_subplot(2,1,1)

ax.errorbar(z,w[:,0],yerr=[w[:,0]-w[:,2],w[:,3]-w[:,0]],
	marker='o',markersize=5,capsize=4,capthick=2,color=colors[0],
	label=r'JLA+BAO-Z16+H(z)+{\it Planck 2015} distance prior}')

ax.hlines(-1,xmin=0.0,xmax=zmax,linestyle='dashed',color='k',lw=2,alpha=0.5)

xlim(-0.05,zmax+0.05)
ylim(-2.75,0.25)
xticks([0,0.5,1.0,1.5,2,2.5])
yticks([-2.5,-2,-1.5,-1.0,-0.5,0])
xlabel(r'$z$',fontsize=13)
ylabel(r'$w(z)$',fontsize=13)
tick_params(axis='both',direction='in')

lgd=legend(loc='upper left',frameon=False,fontsize=12)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],fontsize=13,color=colors[i])


lgd=legend(loc='upper left',frameon=False,fontsize=12)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],fontsize=13,color=colors[i+2])

ax.hlines(-1,xmin=0.0,xmax=1.6,linestyle='dashed',color='k',lw=2,alpha=0.5)

subplots_adjust(left=0.125,
                right=0.975,
                top=0.995,
                hspace=0.0,
                bottom=0.075)



savefig('eos_zhao16.pdf')

show()
