from pylab import *

n_cross = loadtxt('cross_times.txt')

idx_good = n_cross[:,0] <= 0
idx_bad1 = n_cross[:,0] >= 1
idx_bad2 = n_cross[:,1] >= 1

### do not forget to remove idx_bad2 from idx_bad1

idx_bad1_tmp = idx_bad1

for i in range(len(idx_bad1)):
	if idx_bad2[i] == True:
		idx_bad1_tmp[i] = False

idx_bad1 = idx_bad1_tmp


print('sum(idx_good) = ', sum(idx_good))
print('sum(idx_bad1) = ', sum(idx_bad1))
print('sum(idx_bad2) = ', sum(idx_bad2))

p = loadtxt('p_all.txt')

p_all = p[:,0]
p_sne = p[:,1]


#chi2 = loadtxt('chisq.txt')
chi2 = loadtxt('combined_chisq.txt')
chi2_tot = chi2[:,0]
chi2_prior = chi2[:,1]
chi2_data  = chi2[:,2]

fig = figure(figsize=(6,5))

colors=['g','b','r']

nullfmt = NullFormatter()

left, width = 0.125,0.7
bottom, height = left, width
bottom_h = left_h = left + width

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.15]
rect_histy = [left_h, bottom, 0.15, height]

axScatter = axes(rect_scatter)
axHistx = axes(rect_histx)
axHisty = axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHistx.yaxis.set_major_formatter(nullfmt)

axHisty.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot: p vs chisq_tot
axScatter.scatter(p_all[idx_good],chi2_tot[idx_good],marker='x',s=20,color=colors[0],alpha=0.65,label=r'all $w_i$: $< 1\sigma$')
axScatter.scatter(p_all[idx_bad1],chi2_tot[idx_bad1],marker='+',s=35,color=colors[1],alpha=0.50,label=r'at least one $w_i$: $\geq 1\sigma$ and $< 2\sigma$')
axScatter.scatter(p_all[idx_bad2],chi2_tot[idx_bad2],marker='o',s=20,color='',edgecolors=colors[2],label=r'at least one $w_i$: $\geq 2\sigma$',alpha=1)
axScatter.scatter(p_all[79],chi2_tot[79],marker='*',s=150,linewidths=1.5,color='',edgecolors='k')

DY = 0

axScatter.set_xlabel(r'$p$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\rm tot}$',fontsize=14)
axScatter.set_xlim(-0.025,1.025)
axScatter.set_ylim(650,1000+DY)
axScatter.tick_params(axis='both',direction='in')

lgd=axScatter.legend(loc='upper right',bbox_to_anchor=(1.015, 0.95),frameon=False)
texts = lgd.get_texts()
setp(texts[0],fontsize=10,color=colors[0])
setp(texts[1],fontsize=10,color=colors[1])
setp(texts[2],fontsize=10,color=colors[2])

axScatter.text(0.25,980+DY,r'Deviations from $w=-1$',fontsize=11)


bins=30

p_stack = []
p_stack.append(p_all[idx_good])
p_stack.append(p_all[idx_bad1])
p_stack.append(p_all[idx_bad2])

alpha=0.65

axHistx.hist(p_stack,bins=bins,histtype='bar',linewidth=2,color=colors,stacked=True,alpha=alpha)

#axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_xlim(-0.025,1.025)
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHistx.tick_params(axis='x',direction='in')

chi2_data_stack = []
chi2_data_stack.append(chi2_tot[idx_good])
chi2_data_stack.append(chi2_tot[idx_bad1])
chi2_data_stack.append(chi2_tot[idx_bad2])

axHisty.hist(chi2_data_stack,bins=bins,histtype='bar',linewidth=2,color=colors,orientation='horizontal',stacked=True,alpha=alpha)
axHisty.set_xticks([])
axHisty.set_ylim(650,1000+DY)
axHisty.tick_params(axis='y',direction='in')

fig.savefig('p_vs_chi2_tot.pdf')

show()
