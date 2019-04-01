from pylab import *

chi2_lcdm = loadtxt('chisq_lcdm.txt')
chi2_wzcdm = loadtxt('chisq.txt')

chi2_diff_a = []
chi2_diff_b = []
chi2_prior = []

for i in range(len(chi2_lcdm)):
	chi2_diff_a.append(chi2_wzcdm[i,0]-chi2_lcdm[i])
	chi2_diff_b.append(chi2_wzcdm[i,2]-chi2_lcdm[i])
	chi2_prior.append(chi2_wzcdm[i,1])

# plot(chi2_diff_a,'bo',label=r'$\Delta \chi^2_{\rm tot}$')
# plot(chi2_diff_b,'rx',label=r'$\Delta \chi^2_{\rm data}$')
# hlines(0,xmin=0,xmax=100)

figure(figsize=(6,3.25))

hist(chi2_diff_b,bins=30,histtype='bar',rwidth=0.85,color='b',alpha=0.75,label=r'$\Delta \chi^2_{\rm data}$')
hist(chi2_diff_a,bins=30,histtype='bar',rwidth=0.85,color='r',alpha=0.75,label=r'$\Delta \chi^2_{\rm tot}$')

legend(loc='best',frameon=False,fontsize=12)
xlabel(r'$\Delta \chi^2$',fontsize=12)
tick_params(axis='both',direction='in')

# plot(chi2_prior,chi2_diff_b,'ro')

subplots_adjust(top=0.995,bottom=0.15)

savefig('delta_chi2_hist.pdf')
show()