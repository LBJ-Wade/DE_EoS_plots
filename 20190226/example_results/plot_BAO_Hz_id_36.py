from pylab import *
from scipy.interpolate import interp1d

def read_JLA_mock( mock_filename ):
	fp = open(mock_filename,'r')
	lines = fp.readlines()
	fp.close()

	snls3 = []
	for line in lines:
		sn = line.split()
		temp = []
		temp.append(float(sn[1]))
		temp.append(float(sn[2]))
		temp.append(float(sn[3]))
		temp.append(float(sn[4]))
		snls3.append(temp)

	return np.array(snls3)

Hz_best_fit_lcdm = loadtxt('/Users/xyh/GitHub/ClassMC-dev/best_fit/LCDM_Hz.txt')
Hz_best_fit_wzcdm = loadtxt('/Users/xyh/GitHub/ClassMC-dev/best_fit/wzCDM_Hz.txt')
Hz_lcdm = interp1d(Hz_best_fit_lcdm[:,0],Hz_best_fit_lcdm[:,1])
Hz_wzcdm = interp1d(Hz_best_fit_wzcdm[:,0],Hz_best_fit_wzcdm[:,1])


bao_best_fit_lcdm = loadtxt('/Users/xyh/GitHub/ClassMC-dev/best_fit/LCDM_BAO.txt')
bao_best_fit_wzcdm = loadtxt('/Users/xyh/GitHub/ClassMC-dev/best_fit/wzCDM_BAO.txt')
DA_lcdm = interp1d(bao_best_fit_lcdm[:,0],bao_best_fit_lcdm[:,6])
DA_wzcdm = interp1d(bao_best_fit_wzcdm[:,0],bao_best_fit_wzcdm[:,6])


z_ref = linspace(1e-3,2.55,30)

#######################
# configure figure size
fig = figure(figsize=(6,5))

colors = ['gray','g','y']

#######################
# load BAO measurments
rd_fid_lcdm = 150.617
rd_fid_wzcdm = 150.586

# bao_dr12 = loadtxt('/Users/xyh/GitHub/ClassMC-dev/mock_samples/GenBAOs/template/DR12_tomoBAO_Zhao_measurement.txt')
# DA_lya = loadtxt('/Users/xyh/GitHub/ClassMC-dev/data/BAO/Lya.txt')
bao_dr12 = loadtxt('/Users/xyh/GitHub/ClassMC-dev/mock_samples/GenBAOs/mock_Dr12_BAO_20190226/DR12_36.dat')
DA_lya = loadtxt('/Users/xyh/GitHub/ClassMC-dev/mock_samples/GenBAOs/mock_z2.34/LyAlpha_36.dat')

MB = -1.9346420E+01
sn_data = read_JLA_mock('/Users/xyh/GitHub/ClassMC-dev/mock_samples/mock_JLA_20190227_full_cov/MOCK_JLA_36.txt')
sn_z = sn_data[:,0]
sn_mu = sn_data[:,1] + (MB+19.3)
sn_DL = 10**(sn_mu/5)*1e-5
sn_DA = sn_DL/(1+sn_z)**2

bao_z = bao_dr12[:9,0]
bao_dr12_DA = bao_dr12[:9,1]*rd_fid_lcdm 
bao_dr12_Hz = bao_dr12[9:,1]/rd_fid_lcdm 

bao_dr12_DA_err = loadtxt('BAO_DA_rs_std.txt')
bao_dr12_DA_err *= rd_fid_lcdm

ax = fig.add_subplot(2,1,1)

ax.plot(sn_z,sn_DA/DA_lcdm(sn_z),'.',color=colors[0],alpha=0.4,label='JLA SNe Ia')
ax.errorbar(bao_z,bao_dr12_DA/DA_lcdm(bao_z),yerr=bao_dr12_DA_err/DA_lcdm(bao_z),fmt='o',color=colors[1],label=r'DR12 BAO')
ax.errorbar(DA_lya[0],DA_lya[1]/DA_lcdm(DA_lya[0]),yerr=DA_lya[2]/DA_lcdm(DA_lya[0]),fmt='d',color=colors[2],label=r'Ly-$\alpha$ forest')
ax.plot(z_ref,DA_lcdm(z_ref)/DA_lcdm(z_ref),'b--')
ax.plot(z_ref,DA_wzcdm(z_ref)/DA_lcdm(z_ref),'r-')

ax.set_xlim(-0.025,2.525)
ax.set_xticks([])
ax.set_xlabel(r'$Z$')
ax.set_ylim(0.8975,1.1025)
yticks = [0.9,0.95,1.0,1.05,1.1]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)
ax.set_ylabel(r'$D_{A}(z)/D_{A,LCDM}(z)$',fontsize=13)
ax.legend(loc='upper right',ncol=1,frameon=True,fontsize=13)
# ax.grid(linestyle='dashed')

#######################
# load H(z)
bao_dr12_Hz_err = loadtxt('BAO_DA_rs_std.txt')
bao_dr12_Hz_err /= rd_fid_lcdm

# Hz_data = loadtxt('/Users/xyh/GitHub/ClassMC-dev/mock_samples/GenHz/template/Hz_all.dat')
Hz_data = loadtxt('/Users/xyh/GitHub/ClassMC-dev/mock_samples/GenHz/mock_Hz_20190226/Hz_36.dat')
Hz_z = Hz_data[:,0]

ax = fig.add_subplot(2,1,2)
ax.errorbar(bao_z,bao_dr12_Hz/Hz_lcdm(bao_z),yerr=bao_dr12_Hz_err/Hz_lcdm(bao_z),fmt='d',color=colors[1],label=r'DR12 BAO')
ax.errorbar(Hz_z,Hz_data[:,1]/Hz_lcdm(Hz_z),yerr=Hz_data[:,2]/Hz_lcdm(Hz_z),fmt='o',color=colors[0],label='OHD')
ax.plot(z_ref,Hz_lcdm(z_ref)/Hz_lcdm(z_ref),'b--')
ax.plot(z_ref,Hz_wzcdm(z_ref)/Hz_lcdm(z_ref),'r-')

ax.set_xlim(-0.025,2.525)
xticks = [0,0.5,1,1.5,2,2.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)
ax.set_xlabel(r'$Z$')
ax.set_ylim(0.74,1.26)
yticks = [0.8,0.9,1.0,1.1,1.2]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)
ax.set_ylabel(r'$H(z)/H_{LCDM}(z)$',fontsize=13)
ax.legend(loc='upper right',ncol=1,frameon=True,fontsize=13)
# ax.grid(linestyle='dashed')

fig.subplots_adjust(top=0.995,left=0.125,right=0.975,bottom=0.1,hspace=0)

fig.savefig('example_fit_BAO_Hz.pdf')

show()