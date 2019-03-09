from pylab import *

n_cross = loadtxt('cross_times.txt')

idx1 = n_cross > 5
idx2 = n_cross > 10
idx3 = n_cross > 15
idx4 = n_cross > 20

p = loadtxt('p_all.txt')

p_all = p[:,0]
p_sne = p[:,1]


chi2 = loadtxt('chisq.txt')
chi2_all = chi2[:,0]
chi2_prior = chi2[:,1]
chi2_data  = chi2[:,2]

fig = figure(figsize=(11,5))

xticks = [0,0.2,0.4,0.6,0.8,1.0]

ax = fig.add_subplot(1,2,1)
ax.plot(p_all,chi2_data,'ro',label=r'All')
ax.plot(p_sne,chi2_data,'b+',ms=8,markeredgewidth=3,label=r'SNe')

lgd=ax.legend(loc='upper left',fontsize=13)
texts = lgd.get_texts()
setp(texts[0],fontsize=14,color='r')
setp(texts[1],fontsize=14,color='b')

ax.set_xlabel(r'$p$-value',fontsize=13)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)

ax.set_ylabel(r'$\chi^2_{\rm data}$',fontsize=14)
yticks = [700,750,800,850,900]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)

ax.tick_params(axis='both',direction='in')

ax = fig.add_subplot(1,2,2)
ax.plot(p_all,chi2_prior,'ro',label=r'All')
# ax.plot(p_all[idx1],chi2_prior[idx1],'rd',label=r'All')
# ax.plot(p_all[idx2],chi2_prior[idx2],'rs',label=r'All')
# ax.plot(p_all[idx3],chi2_prior[idx3],'rx',label=r'All')
# ax.plot(p_all[idx4],chi2_prior[idx4],'rv',label=r'All')
ax.plot(p_sne,chi2_prior,'b+',ms=8, markeredgewidth=3,label=r'SNe')

# ax.legend(loc='best',shadow=True)
ax.set_xlabel(r'$p$-value',fontsize=13)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)

ax.set_ylabel(r'$\chi^2_{\rm prior}$',fontsize=14)
yticks = [5,6,7,8,9,10]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)

ax.tick_params(axis='both',direction='in')

fig.subplots_adjust(left=0.075,right=0.975,top=0.975,wspace=0.15)
fig.savefig('p_vs_chi2.pdf')
show()