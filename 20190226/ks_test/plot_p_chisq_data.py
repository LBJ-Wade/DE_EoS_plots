from pylab import *

n_cross = loadtxt('cross_times_sigmas.txt')

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

#p = loadtxt('p_all.txt')
p = loadtxt('p_all_updated.txt')

p_all = p[:,0]
p_sne = p[:,1]


chi2_lcdm = loadtxt('combined_chisq_lcdm_updated.txt')
chi2 = loadtxt('combined_chisq.txt')
chi2_tot = chi2[:,0]
chi2_prior = chi2[:,4]
chi2_data  = chi2_tot-chi2_prior
dchi2_tot = chi2[:,0]-chi2_lcdm[:,0]
dchi2_data = chi2[:,0]-chi2_lcdm[:,0] -chi2_prior

fig = figure(figsize=(8,5))

colors=['g','b','r']

nullfmt = NullFormatter()

left    = 0.075
bottom  = 0.1
width   = 0.4
height1 = 0.65
height2 = 0.15

rect_scatter1 = [left, bottom, width, height1]
rect_scatter2 = [left+width, bottom, width, height1]

rect_histx1 = [left, bottom+height1, width, height2]
rect_histx2 = [left+width, bottom+height1, width, height2]

rect_histy = [left+2*width, bottom, (1-0.025-left-2*width), height1]

axScatter1 = axes(rect_scatter1)
axScatter2 = axes(rect_scatter2)

axHistx1 = axes(rect_histx1)
axHistx2 = axes(rect_histx2)

axHisty = axes(rect_histy)

# no labels
axHistx1.xaxis.set_major_formatter(nullfmt)
axHistx1.yaxis.set_major_formatter(nullfmt)

axHistx2.xaxis.set_major_formatter(nullfmt)
axHistx2.yaxis.set_major_formatter(nullfmt)

axHisty.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

## the scatter plot: p vs chisq_tot
axScatter1.scatter(chi2_tot[idx_good],p_all[idx_good],marker='x',s=20,color=colors[0],edgecolors='',alpha=0.45,label=r'Weak-wiggle group')
axScatter1.scatter(chi2_tot[idx_bad1],p_all[idx_bad1],marker='o',s=15,color=colors[1],edgecolors='',alpha=0.35,label=r'Moderate-wiggle group')
axScatter1.scatter(chi2_tot[idx_bad2],p_all[idx_bad2],marker='s',s=20,color=colors[2],edgecolors='',alpha=0.65,label=r'Strong-wiggle group')
axScatter1.scatter(chi2_tot[79],p_all[79],marker='o',s=75,color='b')

axScatter1.set_xlabel(r'$\chi^2_{\rm tot}$',fontsize=12)
axScatter1.set_ylabel(r'$p$',fontsize=14)
axScatter1.set_xlim(625,925)
axScatter1.set_ylim(-0.05,1.05)
axScatter1.tick_params(axis='both',direction='in')
#axScatter1.set_xticks([700,750,800,850,900])
axScatter1.set_xticks([675,725,775,825,875])
axScatter1.text(0.1,0.95,'(a)',horizontalalignment='center',verticalalignment='center', transform=axScatter1.transAxes,fontsize=14)

lgd=axScatter1.legend(loc='upper right',ncol=3,bbox_to_anchor=(2.25, 1.375),frameon=True,title_fontsize=13)
texts = lgd.get_texts()
setp(texts[0],fontsize=12,color=colors[0])
setp(texts[1],fontsize=12,color=colors[1])
setp(texts[2],fontsize=12,color=colors[2])

#############################################################
axScatter2.scatter(dchi2_data[idx_good],p_all[idx_good],marker='x',s=20,color=colors[0],edgecolors='',alpha=0.45)
axScatter2.scatter(dchi2_data[idx_bad1],p_all[idx_bad1],marker='o',s=15,color=colors[1],edgecolors='',alpha=0.35)
axScatter2.scatter(dchi2_data[idx_bad2],p_all[idx_bad2],marker='s',s=20,color=colors[2],edgecolors='',alpha=0.65)
axScatter2.scatter(dchi2_data[79],p_all[79],marker='o',s=75,color='b')

axScatter2.set_xlabel(r'$\Delta\chi^2_{\rm data}$',fontsize=12)
axScatter2.set_yticklabels([])
axScatter2.tick_params(axis='both',direction='in')

axScatter2.text(0.1,0.95,'(b)',horizontalalignment='center',verticalalignment='center', transform=axScatter2.transAxes,fontsize=14)


#############################################################
bins=30
alpha=0.65

p_stack = []
p_stack.append(p_all[idx_good])
p_stack.append(p_all[idx_bad1])
p_stack.append(p_all[idx_bad2])

chi2_tot_stack = []
chi2_tot_stack.append(chi2_tot[idx_good])
chi2_tot_stack.append(chi2_tot[idx_bad1])
chi2_tot_stack.append(chi2_tot[idx_bad2])

dchi2_data_stack = []
dchi2_data_stack.append(dchi2_data[idx_good])
dchi2_data_stack.append(dchi2_data[idx_bad1])
dchi2_data_stack.append(dchi2_data[idx_bad2])

axHisty.hist(p_stack,bins=bins,histtype='bar',linewidth=2,color=colors,orientation='horizontal',stacked=True,alpha=alpha)
axHisty.set_ylim(-0.05,1.05)
axHisty.tick_params(axis='both',direction='in')

axHisty.text(0.825,0.95,'(c)',horizontalalignment='center',verticalalignment='center', transform=axHisty.transAxes,fontsize=14)

############################################################
axHistx1.hist(chi2_tot_stack,bins=bins,histtype='bar',linewidth=2,color=colors,stacked=True,alpha=alpha)
axHistx1.set_yticks([])
axHistx1.set_xlim(625,925)
axHistx1.tick_params(axis='both',direction='in')
axHistx1.text(0.1,0.8,'(d)',horizontalalignment='center',verticalalignment='center', transform=axHistx1.transAxes,fontsize=14)

############################################################
density_flag = False
axHistx2.hist(dchi2_data_stack,bins=bins,histtype='bar',linewidth=2,color=colors,stacked=True,alpha=alpha)

axHistx2.set_yticks([])
#axHistx2.set_xlim(650,950)
axHistx2.tick_params(axis='both',direction='in')
axHistx2.text(0.1,0.8,'(e)',horizontalalignment='center',verticalalignment='center', transform=axHistx2.transAxes,fontsize=14)


############################################################

fig.savefig('p_vs_chi2_dchi2.pdf')

show()
