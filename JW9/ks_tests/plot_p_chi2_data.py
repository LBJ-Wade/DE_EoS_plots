import sys,os
from pylab import *
from scipy.stats import kstest
from matplotlib.ticker import NullFormatter
from ReadMock import *

def extract_bestfit_w(likestats_file):
	tmp = []
	fp = open(likestats_file,'r')
	lines = fp.readlines()
	for i in range(len(lines)):
		if i>=9 and i <= 28:
			tmp.append(float(lines[i].split()[1]))
	fp.close()
	# print(tmp)
	return array(tmp)

prior_inv_covmat = 'CPZ_prior_smoothed_ac_0.06_sigma_mw_0.04_inv.txt'

SN_dir = 'mock_JLA_20190220'

# EoS_dir = 'EoS.old'
EoS_dir = 'EoS.ref_20190220'

# Result_dir = 'results.old'
Result_dir = 'results.ref_20190220'

SIZE=1000

# 740 SNe
# CMB distance prior parameter, 3 
# 20 {wi}, H0, omegac, omegab, MB
dof = (740+3-20-4)

p_value = None
tot_chi2 = None
prior_chi2 = None
nbad = None

if os.path.isfile('CHI2-tot.txt') and \
	os.path.isfile('CHI2-prior.txt') and \
	os.path.isfile('PVAL.txt') and \
	os.path.isfile('NBAD.txt'):
	tot_chi2= loadtxt('CHI2-tot.txt')
	prior_chi2 = loadtxt('CHI2-prior.txt')
	p_value = loadtxt('PVAL.txt')
	nbad = loadtxt('NBAD.txt')
else:
	if os.path.isfile('CHI2-prior.txt') is False:
		print('--> re-calculating prior chi2 ...')
		print('--> loading the covariance matrix for the continuity prior ...')
		inv_covmat = loadtxt(prior_inv_covmat)
		prior_chi2 = []
		for i in range(1,1+SIZE):
			w_best = extract_bestfit_w(Result_dir+'/EoS_'+str(i)+'.likestats')
			chi2 = matmul(matmul(w_best.reshape(1,20),inv_covmat),w_best.reshape(20,1))
			prior_chi2.append(float(chi2))

		prior_chi2 = array(prior_chi2)
		savetxt('CHI2-prior.txt',prior_chi2,fmt='%10.8f',delimiter=' ')
	else:
		prior_chi2= loadtxt('CHI2-prior.txt')

	if os.path.isfile('CHI2-tot.txt') is False:
		print('--> re-calculating data chi2 ...')
		tot_chi2 = []
		for i in range(1,1+SIZE):
			fp = open(Result_dir+'/EoS_'+str(i)+'.likestats','r')
			lines = fp.readlines()
			tot_chi2.append(float(lines[0].split()[-1]))
			fp.close()
	    
		tot_chi2 = array(tot_chi2)
		savetxt('CHI2-tot.txt',tot_chi2,fmt='%10.8f',delimiter=' ')
	else:
		tot_chi2= loadtxt('CHI2-tot.txt')

	if os.path.isfile('PVAL.txt') is False:
		print('--> re-calculating p-values ...')
		p_value = []
		for i in range(1,1+SIZE):
			sn = read_jla_mock(SN_dir+'/MOCK_JLA_'+str(i)+'.txt')
			dmu = (sn[:,1]-sn[:,3])/sn[:,2]
			s,p = kstest(dmu,'norm')
			p_value.append(p)
		    
		p_value = array(p_value)
		savetxt('PVAL.txt',p_value,fmt='%10.8f',delimiter=' ')
	else:
		p_value = loadtxt('PVAL.txt')
	
	if os.path.isfile('NBAD.txt') is False:
		print('--> re-calculating NBAD ...')
		nbad = []
		for i in range(1,1+SIZE):
			eos = loadtxt(EoS_dir+'/eos_'+str(i)+'.txt')
			nbad.append( sum( abs( (eos[:,0]+1)/eos[:,1] ) >= 1.0 ) )
		    
		nbad = array(nbad)
		savetxt('NBAD.txt',nbad,fmt='%10.8f',delimiter=' ')
	else:
		nbad = loadtxt('NBAD.txt')

# get REAL data chi2 by substracting prior_chi2 from tot_chi2
data_chi2 = tot_chi2 - prior_chi2


# start making plots ...

nullfmt = NullFormatter()

left, width = 0.125,0.7
bottom, height = left, width
bottom_h = left_h = left + width

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.15]
rect_histy = [left_h, bottom, 0.15, height]

# start with a rectangular Figure
fig = figure(figsize=(6,5))

axScatter = axes(rect_scatter)
axHistx = axes(rect_histx)
axHisty = axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHistx.yaxis.set_major_formatter(nullfmt)

axHisty.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot
# axScatter.scatter(p_value,data_chi2/dof,marker='o',s=13,color='r',alpha=0.35)
axScatter.scatter(p_value[nbad<=1],data_chi2[nbad<=1]/dof,marker='o',s=13,color='r',alpha=0.65)
axScatter.scatter(p_value[nbad>1],data_chi2[nbad>1]/dof,marker='+',s=35,color='b',alpha=0.85)
axScatter.set_xlabel(r'$p$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\rm reduced} \,\,\,(dof = '+str(dof)+')$',fontsize=14)
axScatter.tick_params(axis='both',direction='in')

bins=40
# axHistx.hist(p_value,bins=bins,rwidth=0.8,color='r',alpha=0.55)
axHistx.hist(p_value[nbad<=1],bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65)
axHistx.hist(p_value[nbad>1],bins=bins,histtype='step',linewidth=2,color='b',alpha=0.85)
axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHistx.tick_params(axis='x',direction='in')

n,b,p=axHisty.hist(data_chi2[nbad<=1]/dof,bins=bins,histtype='step',linewidth=2,color='r',alpha=0.65,orientation='horizontal')
axHisty.hist(data_chi2[nbad>1]/dof,bins=b,histtype='step',linewidth=2,color='b',alpha=0.85,orientation='horizontal')
axHisty.set_xticks([])
axHisty.tick_params(axis='y',direction='in')

fig.savefig('pvalue_vs_chi2_data.pdf')

show()

