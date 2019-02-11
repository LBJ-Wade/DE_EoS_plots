from pylab import *

a = linspace(1,0.4,20)
z = 1/a-1


union= loadtxt('wmap9dp_union_bao_hz_h0_a_2.0_sm_0.04.txt')
snls = loadtxt('wmap9dp_snls3_bao_h0_hz_a_2.0_sm_0.04.txt')
jla1 = loadtxt('wmap9dp_jla_bao_hz_h0_a_2.0_sm_0.04.txt')
jla2 = loadtxt('wmap9dp_jla_bao_hz_a_2.0_sm_0.02_0.04.txt')


# errorbar(z+0.005,union[:,0],yerr=union[:,1])
# fill_between(z,y1=union[:,2],y2=union[:,3],label='UNION+WMAP9',alpha=0.5,facecolor='blue')

# errorbar(z-0.005,snls[:,0],yerr=snls[:,1])
# fill_between(z,y1=snls[:,2],y2=snls[:,3],label='SNLS3+WMAP9',alpha=0.5,facecolor='green')

errorbar(z+0.005,jla1[:,0],yerr=jla1[:,1])
fill_between(z,y1=jla1[:,2],y2=jla1[:,3],label='JLA1+WMAP9',alpha=0.5)

errorbar(z+0.005,jla2[:,0],yerr=jla2[:,1])
fill_between(z,y1=jla2[:,2],y2=jla2[:,3],label='JLA+WMAP9',alpha=0.5,facecolor='red')

legend(loc='best',frameon=False)

xlim(-0.05,1.55)

show()