from pylab import *

bins=15
alpha = 0.65
fig = figure(figsize=(11,4.5))

frac_threshold = 0.8

def scale_factor(n,N):
	return 1./(n/N)**0.5

#####################################################################
ax = fig.add_subplot(1,2,1)

# evec = loadtxt('JLA_WMAP9_MP_vecs.txt')
evec = loadtxt('JLA_WMAP9_SP_vecs.txt')
#evec = loadtxt('JLA_WMAP9_vecs.txt')

frac1_ = []
frac2_ = []
frac3_ = []
frac4_ = []
frac5_ = []
frac6_ = []
frac1 = []
frac2 = []
frac3 = []
frac4 = []
frac5 = []
frac6 = []

for i in range(1,101):
    w = loadtxt('EoS.old/eos_'+str(i)+'.txt')
    dw= w[:,0]+1
    dw /= norm(dw)
    f0_ = matmul(dw,evec[19,:])
    f1_ = matmul(dw,evec[18,:])
    f2_ = matmul(dw,evec[17,:])
    f3_ = matmul(dw,evec[16,:])
    f4_ = matmul(dw,evec[15,:])
    f5_ = matmul(dw,evec[14,:])
    
    f0 = matmul(dw,evec[0,:])
    f1 = matmul(dw,evec[1,:])
    f2 = matmul(dw,evec[2,:])
    f3 = matmul(dw,evec[3,:])
    f4 = matmul(dw,evec[4,:])
    f5 = matmul(dw,evec[5,:])

    frac1_.append( abs(f0_) * scale_factor(1,20) )
    frac2_.append( (f1_**2 + f0_**2)**0.5* scale_factor(2,20) )
    frac3_.append( (f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(3,20) )
    frac4_.append( (f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(4,20) )
    frac5_.append( (f4_**2 + f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(5,20) )
    frac6_.append( (f5_**2 + f4_**2 + f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(6,20) )
    
    frac1.append( abs(f0) * scale_factor(1,20) )
    frac2.append( (f1**2 + f0**2)**0.5 * scale_factor(2,20))
    frac3.append( (f2**2 + f1**2 + f0**2)**0.5* scale_factor(3,20) )
    frac4.append( (f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(4,20) )
    frac5.append( (f4**2 + f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(5,20) )
    frac6.append( (f5**2 + f4**2 + f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(6,20) )

frac1_ = array(frac1_)
frac2_ = array(frac2_)
frac3_ = array(frac3_)
frac4_ = array(frac4_)
frac5_ = array(frac5_)
frac6_ = array(frac6_)
frac1 = array(frac1)
frac2 = array(frac2)
frac3 = array(frac3)
frac4 = array(frac4)
frac5 = array(frac5)
frac6 = array(frac6)

f1_ = sum(frac1_>frac_threshold)/100.
f2_ = sum(frac2_>frac_threshold)/100.
f3_ = sum(frac3_>frac_threshold)/100.
f4_ = sum(frac4_>frac_threshold)/100.
f5_ = sum(frac5_>frac_threshold)/100.
f6_ = sum(frac6_>frac_threshold)/100.

f1 = sum(frac1>frac_threshold)/100.
f2 = sum(frac2>frac_threshold)/100.
f3 = sum(frac3>frac_threshold)/100.
f4 = sum(frac4>frac_threshold)/100.
f5 = sum(frac5>frac_threshold)/100.
f6 = sum(frac6>frac_threshold)/100.

# n1,b1,h1=hist(frac3, bins=bins, density=False, histtype='bar', color='g', label=r'3 WPCs, '+r'$F_3('+str(frac_threshold)+')='+str(round(f3,2))+'$',alpha=alpha)
# n2,b2,h2=hist(frac4, bins=bins, density=False, histtype='bar', color='m', label=r'4 WPCs, '+r'$F_4('+str(frac_threshold)+')='+str(round(f4,2))+'$',alpha=alpha)
n1,b1,h1=hist(frac3, bins=bins, density=False, histtype='bar', color='g', label=r'3 WPCs',alpha=alpha)
n2,b2,h2=hist(frac4, bins=bins, density=False, histtype='bar', color='m', label=r'4 WPCs',alpha=alpha)
# n3,b3,h3=hist(frac6, bins=bins, density=False, histtype='bar', color='k', label=r'6 WPCs',alpha=alpha)
n1_,b1_,h1_=hist(frac3_*1e1, bins=bins, density=False, color='b', histtype='step', lw=2,label=r'3 BPCs')
n2_,b2_,h2_=hist(frac4_*1e1, bins=bins, density=False, color='r', histtype='step', lw=2,label=r'4 BPCs')
text(0.5,15,r'$\times 10$',fontsize=14,color='b')
text(0.5,11,r'$\times 10$',fontsize=14,color='r')

lgd=legend(loc='upper center', ncol=2, frameon=False,fontsize=13)
texts = lgd.get_texts()
colors=['g','m','r','b']
for i in range(len(texts)):
    plt.setp(texts[i],fontsize=13,color=colors[i])

ymax=1.05*max(n1_.max(),n2_.max(),n1.max(),n2.max())
ylim(0,ymax)
# xlim(0,1.0)
xlabel(r'$S_{20}^{3,4}$',fontsize=14)
ax=gca()
ax.set_yticks([])
ax.set_title('Data + Prior',fontsize=14)

############################################################
ax = fig.add_subplot(1,2,2)

# evec = loadtxt('JLA_WMAP9_MP_vecs.txt')
# evec = loadtxt('JLA_WMAP9_SP_vecs.txt')
evec = loadtxt('JLA_WMAP9_vecs.txt')

frac1_ = []
frac2_ = []
frac3_ = []
frac4_ = []
frac5_ = []
frac6_ = []
frac1 = []
frac2 = []
frac3 = []
frac4 = []
frac5 = []
frac6 = []

for i in range(1,101):
    w = loadtxt('EoS.old/eos_'+str(i)+'.txt')
    dw= w[:,0]+1
    dw /= norm(dw)
    f0_ = matmul(dw,evec[19,:])
    f1_ = matmul(dw,evec[18,:])
    f2_ = matmul(dw,evec[17,:])
    f3_ = matmul(dw,evec[16,:])
    f4_ = matmul(dw,evec[15,:])
    f5_ = matmul(dw,evec[14,:])
    
    f0 = matmul(dw,evec[0,:])
    f1 = matmul(dw,evec[1,:])
    f2 = matmul(dw,evec[2,:])
    f3 = matmul(dw,evec[3,:])
    f4 = matmul(dw,evec[4,:])
    f5 = matmul(dw,evec[5,:])

    frac1_.append( abs(f0_)* scale_factor(1,20) )
    frac2_.append( (f1_**2 + f0_**2)**0.5* scale_factor(2,20) )
    frac3_.append( (f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(3,20) )
    frac4_.append( (f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(4,20) )
    frac5_.append( (f4_**2 + f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(5,20) )
    frac6_.append( (f5_**2 + f4_**2 + f3_**2 + f2_**2 + f1_**2 + f0_**2)**0.5* scale_factor(6,20) )
    
    frac1.append( abs(f0)* scale_factor(1,20) )
    frac2.append( (f1**2 + f0**2)**0.5* scale_factor(2,20) )
    frac3.append( (f2**2 + f1**2 + f0**2)**0.5* scale_factor(3,20) )
    frac4.append( (f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(4,20) )
    frac5.append( (f4**2 + f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(5,20) )
    frac6.append( (f5**2 + f4**2 + f3**2 + f2**2 + f1**2 + f0**2)**0.5* scale_factor(6,20) )

frac1_ = array(frac1_)
frac2_ = array(frac2_)
frac3_ = array(frac3_)
frac4_ = array(frac4_)
frac5_ = array(frac5_)
frac6_ = array(frac6_)
frac1 = array(frac1)
frac2 = array(frac2)
frac3 = array(frac3)
frac4 = array(frac4)
frac5 = array(frac5)
frac6 = array(frac6)

f1_ = sum(frac1_>frac_threshold)/100.
f2_ = sum(frac2_>frac_threshold)/100.
f3_ = sum(frac3_>frac_threshold)/100.
f4_ = sum(frac4_>frac_threshold)/100.
f5_ = sum(frac5_>frac_threshold)/100.
f6_ = sum(frac6_>frac_threshold)/100.

f1 = sum(frac1>frac_threshold)/100.
f2 = sum(frac2>frac_threshold)/100.
f3 = sum(frac3>frac_threshold)/100.
f4 = sum(frac4>frac_threshold)/100.
f5 = sum(frac5>frac_threshold)/100.
f6 = sum(frac6>frac_threshold)/100.

# n1,b1,h1=hist(frac3, bins=bins, density=False, histtype='bar', color='g', label=r'3 BPCs, '+r'$F_3('+str(frac_threshold)+')='+str(round(f3,2))+'$',alpha=alpha)
# n2,b2,h2=hist(frac4, bins=bins, density=False, histtype='bar', color='m', label=r'4 BPCs, '+r'$F_4('+str(frac_threshold)+')='+str(round(f4,2))+'$',alpha=alpha)
n1,b1,h1=hist(frac3, bins=bins, density=False, histtype='bar', color='g', label=r'3 BPCs',alpha=alpha)
n2,b2,h2=hist(frac4, bins=bins, density=False, histtype='bar', color='m', label=r'4 BPCs',alpha=alpha)
n1_,b1_,h1_=hist(frac3_, bins=bins, density=False, color='r', histtype='step', lw=2,label=r'3 WPCs')
n2_,b2_,h2_=hist(frac4_, bins=bins, density=False, color='b', histtype='step', lw=2,label=r'4 WPCs')


lgd=legend(loc='upper center', ncol=2, frameon=False,fontsize=13)
texts = lgd.get_texts()
colors=['g','m','r','b']
for i in range(len(texts)):
    plt.setp(texts[i],fontsize=13,color=colors[i])

ymax=1.2*max(n1_.max(),n2_.max(),n1.max(),n2.max())
ylim(0,ymax)

xlabel(r'$S_{20}^{3,4}$',fontsize=14)
ax=gca()
ax.set_yticks([])
ax.set_title('Data',fontsize=14)

###################################################


f=gcf()
f.subplots_adjust(left=0.025,right=0.975,bottom=0.145,top=0.9,wspace=0.075)

savefig('Sn_JLA_WMAP9_new.pdf')

show()
