import sys,os
from pylab import *
from scipy.stats import kstest
from matplotlib.ticker import NullFormatter
from ReadMock import *

SIZE=690

SN_dir = 'mock_JLA_20190204'
EoS_dir = 'EoS.ref_20190212'
Result_dir = 'results.ref_20190212'

p_value = None
eos_chi2 = None
nbad = None

if os.path.isfile('CHI2.txt') and os.path.isfile('PVAL.txt') and os.path.isfile('NBAD.txt'):
	p_value = loadtxt('PVAL.txt')
	eos_chi2= loadtxt('CHI2.txt')
	nbad = loadtxt('NBAD.txt')
else:
	if os.path.isfile('CHI2.txt') is False:
		print('--> re-computing chi2-w ...')
		eos_chi2 = []
		for i in range(1,1+SIZE):
			eos_file = EoS_dir+'/eos_'+str(i)+'.txt'
			cov_file= Result_dir+'/EoS_'+str(i)+'.covmat'
			eos = loadtxt(eos_file)
			covmat = loadtxt(cov_file)
			icovmat = inv(covmat[4:,4:])
			deos = eos[:,0]+1
			chi2 = matmul(matmul(deos.reshape(1,20),icovmat),deos.reshape(20,1))
			eos_chi2.append(float(chi2))
		eos_chi2 = array(eos_chi2)
		savetxt('CHI2.txt',eos_chi2,fmt='%10.8f',delimiter=' ')
	else:
		eos_chi2= loadtxt('CHI2.txt')
	
	if os.path.isfile('PVAL.txt') is False:
		print('--> re-computing p-values ...')
		p_value = []
		for i in range(1,1+SIZE):
			sn_file = SN_dir + '/MOCK_JLA_'+str(i)+'.txt'
			sn = read_jla_mock(sn_file)
			dmu = (sn[:,1]-sn[:,3])/sn[:,2]
			s,p = kstest(dmu,'norm')
			p_value.append(p)
		p_value = array(p_value)
		savetxt('PVAL.txt',p_value,fmt='%10.8f',delimiter=' ')
	else:
		p_value = loadtxt('PVAL.txt')

	if os.path.isfile('NBAD.txt') is False:
		print('--> re-computing NBAD ...')
		nbad = []
		for i in range(1,1+SIZE):
			eos = loadtxt(EoS_dir+'/eos_'+str(i)+'.txt')
			nbad.append( sum( abs( (eos[:,0]+1)/eos[:,1] ) >= 1.0 ) )
		nbad = array(nbad)
		savetxt('NBAD.txt',nbad,fmt='%10.8f',delimiter=' ')
	else:
		nbad = loadtxt('NBAD.txt')

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
# axScatter.scatter(p1_value[nbad<=1],eos1_chi2[nbad<=1],s=15,alpha=0.55)
axScatter.scatter(p_value,eos_chi2,marker='o',s=13,color='r',alpha=0.45)
axScatter.scatter(p_value[nbad>1],eos_chi2[nbad>1],marker='x',s=20,color='b',alpha=0.45)

# xticks=[0,0.2,0.4,0.6,0.8,1.0]
# yticks=[0.0,2.5,5.0,7.5,10,12.5,15,17.5]
# axScatter.set_xticks(xticks)
# axScatter.set_yticks(yticks)
# axScatter.set_xticklabels(xticks,fontsize=13)
# axScatter.set_yticklabels(yticks,fontsize=13)


# add a vertical dashed line to indicate the reduced chi2=1
# axScatter.hlines(19,xmin=0,xmax=1,linestyles='dashed',alpha=0.75)
# axScatter.text(0,17,r'reduced $\chi^2_{\mathbf{w}}=1 \,\,(dof=19)$',fontsize=14)

bins=30
axHistx.hist(p_value,bins=bins,rwidth=0.8,color='r',alpha=0.55)
axHistx.hist(p_value[nbad>1],bins=bins,rwidth=0.8,color='b',alpha=0.65)

n,b,p=axHisty.hist(eos_chi2,bins=bins,rwidth=0.8,color='r',alpha=0.55,orientation='horizontal')
axHisty.hist(eos_chi2[nbad>1],bins=b,rwidth=0.8,color='b',alpha=0.65,orientation='horizontal')

axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHisty.set_xticks([])

axScatter.set_xlabel(r'$p$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\mathbf{w}}=(\mathbf{w}+1)\cdot\mathbf{C}^{-1}_{\mathbf{w}}\cdot(\mathbf{w}+1)$',fontsize=14)

fig.savefig('pvalue_vs_chi2_w.pdf')

show()

