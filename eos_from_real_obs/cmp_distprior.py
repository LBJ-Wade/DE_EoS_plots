from pylab import *

a = linspace(1,0.4,20)
z = 1/a-1

a = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.02.txt')
b = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt')
c = loadtxt('wmap9dp_jla_bao_h0_hz_a_2.0_sm_0.02.txt')
d = loadtxt('wmap9dp_jla_bao_h0_hz_a_2.0_sm_0.04.txt')
e = loadtxt('wmap9dp_union_bao_h0_hz_a_2.0_sm_0.02.txt')
f = loadtxt('wmap9dp_union_bao_h0_hz_a_2.0_sm_0.04.txt')

dz = 0.0075

# errorbar(z-1.5*dz,a[:,0],yerr=a[:,1],label='SNLS3,sm=0.02')
# errorbar(z-0.5*dz,b[:,0],yerr=b[:,1],label='SNLS3,sm=0.04')
errorbar(z+0.5*dz,c[:,0],yerr=c[:,1],label='JLA,sm=0.02')
errorbar(z+1.5*dz,d[:,0],yerr=d[:,1],label='JLA,sm=0.04')

errorbar(z+2.5*dz,e[:,0],yerr=e[:,1],label='UNION,sm=0.02')
errorbar(z+3.5*dz,f[:,0],yerr=f[:,1],label='UNION,sm=0.04')

xlim(-0.05,1.55)
ylim(-1.8,0.2)

hlines(-1,xmin=0.0,xmax=1.6,linestyle='dashed',color='gray',lw=2.5)

legend(loc='upper left',frameon=False,fontsize=14)
xlabel(r'$z$',fontsize=16)
ylabel(r'$w(z)$',fontsize=16)

f=gcf()
f.tight_layout()

show()
