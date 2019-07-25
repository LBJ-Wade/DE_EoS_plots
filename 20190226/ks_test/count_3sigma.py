from pylab import *

chi2_lcdm = loadtxt('combined_chisq_lcdm_updated.txt')
chi2_dde  = loadtxt('combined_chisq.txt')
dchi2_tot = chi2_dde[:,0]-chi2_lcdm[:,0]
dchi2_dat = chi2_dde[:,0]-chi2_lcdm[:,0]-chi2_dde[:,4]


chi2_lcdm_f = loadtxt('chisq_lcdm_forecast.txt')
chi2_dde_f  = loadtxt('chisq_dde_forecast.txt')
dchi2_tot_f = chi2_dde_f[:,0]-chi2_lcdm_f
dchi2_dat_f = chi2_dde_f[:,0]-chi2_lcdm_f-chi2_dde_f[:,1]

cnt1 = sum(dchi2_tot<-9)
cnt2 = sum(dchi2_tot_f<-9)


print('cnt1 = %5d'%(cnt1))
print('cnt2 = %5d'%(cnt2))

cnt1 = sum(dchi2_dat<-9)
cnt2 = sum(dchi2_dat_f<-9)


print('cnt1 = %5d'%(cnt1))
print('cnt2 = %5d'%(cnt2))
