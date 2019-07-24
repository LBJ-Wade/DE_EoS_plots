from pylab import *

chi2_lcdm = loadtxt('combined_chisq_lcdm_updated.txt')
chi2_dde  = loadtxt('combined_chisq.txt')

dchi2_tot = chi2_dde[:,0]-chi2_lcdm[:,0]


chi2_lcdm_f = loadtxt('chisq_lcdm_forecast.txt')
chi2_dde_f  = loadtxt('chisq_dde_forecast.txt')

dchi2_tot_f = chi2_dde_f[:,0]-chi2_lcdm_f

#plot(abs(dchi2_tot_f)-abs(dchi2_tot),'.')

hist(abs(dchi2_tot_f)-abs(dchi2_tot),bins=30,density=True,alpha=0.5)

hm = mean(abs(dchi2_tot_f)-abs(dchi2_tot))
h,b=histogram(abs(dchi2_tot_f)-abs(dchi2_tot),bins=30,density=True)

b = (b[1:]+b[0:-1])/2

#plot(b,h,'b-.',label=r'Dist of $|\Delta\chi^2_{\rm \Lambda JDF^{\ast}}|-|\Delta\chi^2_{\rm \Lambda JD16^{\ast}}|$')
vlines(hm,ymin=0,ymax=1.05*max(h),linestyles='solid',lw=5,color='r',alpha=0.5,label=r'Mean value')
vlines(0,ymin=0,ymax=1.05*max(h),linestyles='dashed')
ylim(-0.0005,1.05*max(h))
xlabel(r'$|\Delta\chi^2_{\rm \Lambda JDF^{\ast}}|-|\Delta\chi^2_{\rm \Lambda JD16^{\ast}}|$',fontsize=14)
legend(loc='best')

subplots_adjust(wspace=0,hspace=0,bottom=0.15,top=0.925,left=0.1,right=0.95)

show()
