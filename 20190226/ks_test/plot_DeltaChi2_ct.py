from pylab import *

ct = loadtxt('cross_times.txt')
ct1 = ct[:,0]
ct2 = ct[:,1]

idx1 = ct1 > 0
idx2 = ct2 > 0

chisq_dde = loadtxt('combined_chisq.txt')
chisq_lcdm= loadtxt('combined_chisq_lcdm_updated.txt')

delta_chisq_tot = chisq_dde[:,0] - chisq_lcdm[:,0]
delta_chisq_dat = delta_chisq_tot - chisq_dde[:,4]

delta_chisq_jla = chisq_dde[:,3] - chisq_lcdm[:,3]
delta_chisq_cmb = chisq_dde[:,2] - chisq_lcdm[:,2]
delta_chisq_bao = chisq_dde[:,1] - chisq_lcdm[:,1]


figure(figsize=(10,7))

subplot(2,2,1)
plot(delta_chisq_tot[idx1], ct1[idx1], 'rx', label=r'$\geq 1\sigma$ and $< 2\sigma$')
#plot(delta_chisq_dat[idx1], ct1[idx1], 'b+', label=r'$\Delta\chi^2_{\rm data}$')
plot(delta_chisq_tot[idx2], ct2[idx2], 'b+', label=r'$\geq 2\sigma$')
xlabel(r'$\Delta\chi^2_{\rm tot}$')
ylabel(r'# of deviations')
legend(loc='upper right')

subplot(2,2,2)
plot(delta_chisq_jla[idx1], ct1[idx1], 'rx', label=r'$\Delta\chi^2_{\rm JLA}$')
plot(delta_chisq_jla[idx2], ct2[idx2], 'b+', label=r'$\Delta\chi^2_{\rm JLA}$')
xlabel(r'$\Delta\chi^2_{\rm JLA}$')
ylabel(r'# of deviations')
xlim(-15,3)
#legend(loc='upper left')

subplot(2,2,3)
plot(delta_chisq_cmb[idx1], ct1[idx1], 'rx', label=r'$\Delta\chi^2_{\rm CMB}$')
plot(delta_chisq_cmb[idx2], ct2[idx2], 'b+', label=r'$\Delta\chi^2_{\rm CMB}$')
xlabel(r'$\Delta\chi^2_{\rm CMB}$')
ylabel(r'# of deviations')
xlim(-15,3)
#legend(loc='upper left')

subplot(2,2,4)
plot(delta_chisq_bao[idx1], ct1[idx1], 'rx', label=r'$\Delta\chi^2_{\rm BAO}$')
plot(delta_chisq_bao[idx2], ct2[idx2], 'b+', label=r'$\Delta\chi^2_{\rm BAO}$')
xlabel(r'$\Delta\chi^2_{\rm BAO}$')
ylabel(r'# of deviations')
xlim(-15,3)
#legend(loc='upper left')

tight_layout()
#subplots_adjust(wspace=0.05)

figure()

subplot(2,1,1)
hist(delta_chisq_dat, bins=30, histtype='step', color='r', label=r'$\Delta\chi^2_{\rm dat}$')
hist(delta_chisq_tot, bins=30, histtype='step', color='b', label=r'$\Delta\chi^2_{\rm tot}$')
legend(loc='upper left')

subplot(2,1,2)
plot(delta_chisq_dat, delta_chisq_tot, '.')
xlabel(r'$\Delta\chi^2_{\rm dat}$')
ylabel(r'$\Delta\chi^2_{\rm tot}$')

tight_layout()

show()
