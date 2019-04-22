from pylab import *

n_cross = loadtxt('cross_times.txt')

idx_good = n_cross[:,0] <= 0
idx_bad1 = n_cross[:,0] >= 1
idx_bad2 = n_cross[:,1] >= 1

print('sum(idx_good) = ', sum(idx_good))
print('sum(idx_bad1) = ', sum(idx_bad1))
print('sum(idx_bad2) = ', sum(idx_bad2))

p = loadtxt('p_all.txt')

p_all = p[:,0]
p_sne = p[:,1]


chi2 = loadtxt('chisq.txt')
chi2_all = chi2[:,0]
chi2_prior = chi2[:,1]
chi2_data  = chi2[:,2]

fig = figure(figsize=(6,5))

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

# the scatter plot
axScatter.scatter(p_all[idx_good],chi2_data[idx_good],marker='o',s=15,color='gray',alpha=0.65,label='deviation from $w=-1$ less than $1\sigma$ ')
# axScatter.scatter(p_all,chi2_data,marker='o',s=20,color='gray',alpha=0.25)
axScatter.scatter(p_all[idx_bad1],chi2_data[idx_bad1],marker='+',s=35,color='b',label=r'deviation from $w=-1$ by $\gtrsim 1\sigma$ ',alpha=0.75)
axScatter.scatter(p_all[idx_bad2],chi2_data[idx_bad2],marker='o',s=40,color='',edgecolors='r',label=r'deviation from $w=-1$ by $\gtrsim 2\sigma$ ',alpha=1)
axScatter.scatter(p_all[79],chi2_data[79],marker='*',s=100,color='lime')
axScatter.set_xlabel(r'$p$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\rm data}$',fontsize=14)
axScatter.set_ylim(675,975)
axScatter.tick_params(axis='both',direction='in')

lgd=axScatter.legend(loc='upper right',frameon=False)
texts = lgd.get_texts()
setp(texts[0],fontsize=11,color='gray')
setp(texts[1],fontsize=11,color='b')
setp(texts[2],fontsize=11,color='r')

bins=30
# axHistx.hist(p_value,bins=bins,rwidth=0.8,color='r',alpha=0.55)
# axHistx.hist(p_all[idx_good],bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65)

p_stack = []
p_stack.append(p_all[idx_bad2])
p_stack.append(p_all[idx_bad1])
p_stack.append(p_all[idx_good])

alpha=0.65

axHistx.hist(p_stack,bins=bins,histtype='bar',linewidth=2,color=['r','b','gray'],stacked=True,alpha=alpha)

axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHistx.tick_params(axis='x',direction='in')

chi2_data_stack = []
chi2_data_stack.append(chi2_data[idx_bad2])
chi2_data_stack.append(chi2_data[idx_bad1])
chi2_data_stack.append(chi2_data[idx_good])

axHisty.hist(chi2_data_stack,bins=bins,histtype='bar',linewidth=2,color=['r','b','gray'],orientation='horizontal',stacked=True,alpha=alpha)
axHisty.set_xticks([])
axHisty.set_ylim(675,975)
axHisty.tick_params(axis='y',direction='in')

fig.savefig('p_vs_chi2.pdf')

show()
