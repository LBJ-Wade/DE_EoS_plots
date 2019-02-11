import sys,os
from pylab import *
from scipy.stats import kstest
from matplotlib.ticker import NullFormatter
from ReadMock import *

EoS_dir = 'EoS.old'
Result_dir = 'results.old'

SIZE=100

p_value = None
eos_chi2 = None
nbad = None

if os.path.isfile('CHI2-data.txt') and os.path.isfile('PVAL.txt') and os.path.isfile('NBAD.txt'):
	p_value = loadtxt('PVAL.txt')
	eos_chi2= loadtxt('CHI2-data.txt')
	nbad = loadtxt('NBAD.txt')
else:
	if os.path.isfile('CHI2-data.txt') is False:
		print('--> re-calculating data chi2 ...')
		eos_chi2 = []
		for i in range(1,1+SIZE):
			fp = open(Result_dir+'/EoS_'+str(i)+'.likestats','r')
			lines = fp.readlines()
			eos1_chi2.append(float(lines[0].split()[-1]))
			fp.close()
	    
		eos_chi2 = array(eos_chi2)
		savetxt('CHI2-data.txt',eos_chi2,fmt='%10.8f',delimiter=' ')
	
	if os.path.isfile('PVAL.txt') is False or os.path.isfile('NBAD.txt'):
		print('--> re-calculating p-values ...')
		p_value = []
		nbad = []
		for i in range(1,1+SIZE):
			sn_file = 'mock_JLA_EoS_1000/MOCK_JLA_'+str(i)+'.txt'
			sn = read_jla_mock(sn_file)
			dmu = (sn[:,1]-sn[:,3])/sn[:,2]
			s,p = kstest(dmu,'norm')
			eos_file = EoS_dir+'/eos_'+str(i)+'.txt'
			eos = loadtxt(eos_file)
			nbad.append( sum( abs( (eos[:,0]+1)/eos[:,1] ) >= 1.0 ) )
			p_value.append(p)
		    
		nbad = array(nbad)
		p_value = array(p_value)
		savetxt('PVAL.txt',p_value,fmt='%10.8f',delimiter=' ')
		savetxt('NBAD.txt',nbad,fmt='%10.8f',delimiter=' ')
		

nullfmt = NullFormatter()

left, width = 0.125,0.7
bottom, height = 0.115, 0.7
bottom_h = left_h = left + width + 0.0

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
# print('len(p1_value) = ', len(p1_value))
# print('len(eos1_chi2) = ', len(eos1_chi2))

axScatter.scatter(p_value,eos_chi2,marker='o',s=13,color='r',alpha=0.45)
axScatter.scatter(p_value[nbad>1],eos_chi2[nbad>1],marker='x',s=20,color='b',alpha=0.35)

bins=30
axHistx.hist(p_value,bins=bins,rwidth=0.8,color='r',alpha=0.55)
axHistx.hist(p_value[nbad>1],bins=bins,rwidth=0.8,color='b',alpha=0.65)

n,b,p=axHisty.hist(eos_chi2,bins=bins,rwidth=0.8,color='r',alpha=0.55,orientation='horizontal')
axHisty.hist(eos_chi2[nbad>1],bins=b,rwidth=0.8,color='b',alpha=0.65,orientation='horizontal')

axHistx.set_xlim(axHistx.get_xlim())
axHistx.set_ylim(axHistx.get_ylim())
axHistx.set_yticks([])
axHisty.set_xticks([])

axScatter.set_xlabel(r'$P$',fontsize=14)
axScatter.set_ylabel(r'$\chi^2_{\rm tot}$',fontsize=14)

fig.savefig('pvalue_vs_chi2_data.pdf')

show()

