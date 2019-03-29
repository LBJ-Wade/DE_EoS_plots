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
# legend(loc='best')
# xlabel('Result IDs')
# ylabel(r'$\Delta \chi^2$')

# savefig('delta_chi2.pdf')

plot(chi2_prior,chi2_diff_b,'ro')

show()