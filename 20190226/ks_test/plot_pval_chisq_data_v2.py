from pylab import *

n_cross = loadtxt('cross_times.txt')

idx_good = n_cross <= 0
idx_bad = n_cross >= 1

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
# axScatter.scatter(p_all[idx_good],chi2_data[idx_good],marker='o',s=13,color='r',alpha=0.65,label='No deviation from $w=-1$')
axScatter.scatter(p_all,chi2_data,marker='o',s=13,color='r',alpha=0.65)
axScatter.scatter(p_all[idx_bad],chi2_data[idx_bad],marker='+',s=35,color='b',alpha=0.85,label='Has deviation from $w=-1$')
axScatter.set_xlabel(r'$p$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\rm data}$',fontsize=14)
axScatter.set_ylim(675,975)
axScatter.tick_params(axis='both',direction='in')

lgd=axScatter.legend(loc='upper left',frameon=False)
texts = lgd.get_texts()
setp(texts[0],fontsize=12,color='b')
# setp(texts[1],fontsize=12,color='b')

bins=15
# axHistx.hist(p_value,bins=bins,rwidth=0.8,color='r',alpha=0.55)
# axHistx.hist(p_all[idx_good],bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65)
axHistx.hist(p_all,bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65)
axHistx.hist(p_all[idx_bad],bins=bins,histtype='step',linewidth=2,color='b',alpha=0.85)
axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHistx.tick_params(axis='x',direction='in')

# n,b,p=axHisty.hist(chi2_data[idx_good],bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65,orientation='horizontal')
n,b,p=axHisty.hist(chi2_data,bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65,orientation='horizontal')
axHisty.hist(chi2_data[idx_bad],bins=b,histtype='step',linewidth=2,color='b',alpha=0.85,orientation='horizontal')
axHisty.set_xticks([])
axHisty.set_ylim(675,975)
axHisty.tick_params(axis='y',direction='in')

fig.savefig('p_vs_chi2.pdf')

show()