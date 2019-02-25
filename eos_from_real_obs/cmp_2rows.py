from pylab import *

colors = [u'#1f77b4', u'#ff7f0e', u'#2ca02c', u'#d62728', u'#9467bd', u'#8c564b']

a = linspace(1,0.4,20)
z = 1/a-1

a = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.02.txt')
b = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt')
c = loadtxt('wmap9dp_snls3_bao_hz_h0_a_2.0_sm_0.08.txt')
d = loadtxt('wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt')
d0 = loadtxt('wmap9_snls3_bao_hz_h0_a_2.0_sm_0.04.txt_0')
e = loadtxt('plk2015_snls3_bao_hz_h0_a_2.0_sm_0.04.txt')
f = loadtxt('plk2015_jla_bao_hz_h0_a_2.0_sm_0.04.txt')

dz = 0.0075

fig = figure(figsize=(6,7))

ax = fig.add_subplot(2,1,1)

ax.errorbar(z-dz,b[:,0],yerr=[b[:,0]-b[:,2],b[:,3]-b[:,0]],
	marker='o',markersize=5,capsize=4,capthick=2,color=colors[0],
	label=r'SNLS3+BAO+H(z)+WMAP9 distance prior')

ax.errorbar(z+dz,d[:,0],yerr=[d[:,0]-d[:,2],d[:,3]-d[:,0]],
	marker='s',markersize=5,capsize=4,capthick=2,color=colors[1],
	label=r'SNLS3+BAO+H(z)+WMAP9')

ax.hlines(-1,xmin=0.0,xmax=1.6,linestyle='dashed',color='k',lw=2,alpha=0.5)

xlim(-0.05,1.55)
ylim(-1.75,0.1)
xticks([0,0.25,0.5,0.75,1.0,1.25,1.5])
yticks([-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0])
xlabel(r'$z$',fontsize=13)
ylabel(r'$w(z)$',fontsize=13)
tick_params(axis='both',direction='in')

lgd=legend(loc='upper left',frameon=False,fontsize=12)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],fontsize=13,color=colors[i])

# plot(z,e[:,0],color=colors[2],linestyle='--',lw=3,alpha=0.75)
# plot(z,f[:,0],color=colors[3],linestyle=':',lw=3,alpha=0.75)

ax = fig.add_subplot(2,1,2)

# ax.fill_between(z,y1=e[:,2],y2=e[:,3],color=colors[2],lw=0.1,alpha=0.3,label=r'SNLS3+BAO+H(z)+${\it Planck\,2015}$')
# ax.fill_between(z,y1=f[:,2],y2=f[:,3],color=colors[3],lw=0.1,alpha=0.3,label=r'JLA+BAO+H(z)+${\it Planck\,2015}$')

ax.errorbar(z-dz,e[:,0],yerr=[e[:,0]-e[:,2],e[:,3]-e[:,0]],marker='o',markersize=5,capsize=4,capthick=2,
	color=colors[2],label=r'SNLS3+BAO+H(z)+${\it Planck}$')
ax.errorbar(z+dz,f[:,0],yerr=[f[:,0]-f[:,2],f[:,3]-f[:,0]],marker='s',markersize=5,capsize=4,capthick=2,
	color=colors[3],label=r'JLA+BAO+H(z)+${\it Planck}$')

# ax.set_yticks([])

lgd=legend(loc='upper left',frameon=False,fontsize=12)
texts = lgd.get_texts()
for i in range(len(texts)):
	plt.setp(texts[i],fontsize=13,color=colors[i+2])

ax.hlines(-1,xmin=0.0,xmax=1.6,linestyle='dashed',color='k',lw=2,alpha=0.5)


xlim(-0.05,1.55)
ylim(-1.75,0.1)
xticks([0,0.25,0.5,0.75,1.0,1.25,1.5])
yticks([-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,0])
xlabel(r'$z$',fontsize=13)
ylabel(r'$w(z)$',fontsize=13)
tick_params(axis='both',direction='in')

subplots_adjust(left=0.125,
                right=0.975,
                top=0.995,
                hspace=0.0,
                bottom=0.075)



savefig('cpz_result_2rows.pdf')

show()
