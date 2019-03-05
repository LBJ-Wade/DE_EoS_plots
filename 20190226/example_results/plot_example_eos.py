from pylab import *

w = loadtxt('eos_36.txt')
p_all= '0.50'
p_sn = '0.46'
chisq_lcdm = 806.143988
chisq_wzCDM= 801.835
chisq_prior= 7.21573

# w = loadtxt('eos_37.txt')
# p = 0.83
# chisq_lcdm = 832.693329
# chisq_wzCDM= 831.013

zmax = 2.5
a = linspace(1,1/(1+zmax),30)
z = 1/a-1

fig = figure(figsize=(7,5*(7./8)))

ax = fig.add_subplot(1,1,1)

ax.fill_between(z,y1=w[:,2],y2=w[:,3],color='r',alpha=0.3,label=r'Reconstructed $w(z)$')
ax.plot(z,w[:,2],ls='-',color='r',alpha=0.4)
ax.plot(z,w[:,3],ls='-',color='r',alpha=0.4)
ax.plot(z,w[:,0],ls='-',color='r')

ax.hlines(-1,xmin=0,xmax=zmax,linestyles='--',colors='b',label=r'Fiducial $w=-1$')


ax.set_xlim(-0.025,zmax+0.025)

ax.set_xlabel(r'$z$',fontsize=14)
ax.set_ylabel(r'$w(z)$',fontsize=14)
lgd=ax.legend(loc='upper left',frameon=False,fontsize=14)
texts = lgd.get_texts()
setp(texts[0],fontsize=14,color='r')
setp(texts[1],fontsize=14,color='b')

# text(1.5,-1.25,r'$\chi^2_{\rm LCDM} = ' + str(round(chisq_lcdm,3)) + '$',fontsize=14)
# text(1.5,-1.45,r'$\chi^2_{\rm w(z)CDM} = ' + str(round(chisq_wzCDM,3)) + '$',fontsize=14)

chisq_val = '  %8.3f'%(chisq_prior)
ax.text(1.7,-1.2,r'$\chi^2_{\rm prior}$',fontsize=13)
ax.text(1.95,-1.2,r'$=$',fontsize=13)
ax.text(2.1,-1.2,chisq_val,fontsize=13)

chisq_val = '%8.3f'%(chisq_wzCDM+chisq_prior)
ax.text(1.2,-1.4,r'$\chi^2_{\rm w(z)CDM} + \chi^2_{\rm prior}$',fontsize=13)
ax.text(1.95,-1.4,r'$=$',fontsize=13)
ax.text(2.1,-1.4,chisq_val,fontsize=13)

chisq_val = ' %8.3f'%(chisq_wzCDM-chisq_lcdm)
ax.text(1.2,-1.6,r'$\chi^2_{\rm w(z)CDM} - \chi^2_{\rm LCDM}$',fontsize=13)
ax.text(1.95,-1.6,r'$=$',fontsize=13)
ax.text(2.1,-1.6,chisq_val,fontsize=13)

ax.text(0.075,-0.2,r'$p$-value = '+p_all+' (All)',fontsize=13)
ax.text(0.075,-0.35,r'$p$-value = '+p_sn+' (SNe)',fontsize=13)

xticks = [0,0.5,1,1.5,2,2.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=14)

yticks = [-1.5,-1,-0.5,0]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=14)

fig.subplots_adjust(top=0.995)

fig.savefig('example_w_result.pdf')

# plot BAO and SN fitting

# ax = fig.add_subplot()



show()