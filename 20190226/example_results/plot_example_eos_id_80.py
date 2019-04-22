from pylab import *

# w = loadtxt('post/EoS/eos_34.txt')
w = loadtxt('post_no_extra_w/EoS/eos_80.txt')
w_bestfit = loadtxt('post_no_extra_w/EoS/EoS_80_w_peak_vals.txt')

EoS_no_err_dir = 'post_no_err_sm_0.04/EoS'
EoS_no_err_dir2 = 'post_no_err_sm_0.1/EoS'
w_no_err = loadtxt(EoS_no_err_dir+'/eos_1.txt')
w_peak = loadtxt(EoS_no_err_dir+'/EoS_1_w_peak_vals.txt')


p_all= '0.58'
p_sn = '0.59'
chisq_lcdm = 841.232853
# chisq_wzCDM= 834.04
# chisq_prior= 8.47255
chisq_wzCDM = 834.803
chisq_prior = 6.98254

zmax = 2.5
a = linspace(1,1/(1+zmax),30)
z = 1/a-1

fig = figure(figsize=(6,5))

ax = fig.add_subplot(1,1,1)

ax.fill_between(z,y1=w[:,2],y2=w[:,3],color='r',alpha=0.3,label=r'Reconstructed $w(z)$')
fill_between(z,y1=w_no_err[:,2],y2=w_no_err[:,3],color='gray',alpha=0.25,label=r'Ideal mock dataset: $\Delta \bf{d}=0$')

ax.plot(z,w[:,2],ls='-',color='r',lw=2,alpha=0.75)
ax.plot(z,w[:,3],ls='-',color='r',lw=2,alpha=0.75)
ax.plot(z,w[:,0],ls='-',color='r',lw=3)
# ax.plot(z,w_bestfit,'-o',color='r',lw=3)

# ax.fill_between(z,y1=wx[:,2],y2=wx[:,3],color='g',alpha=0.3,label=r'Reconstructed $w(z)$')

plot(z,w_peak,color='gray',ls='-.',lw=2,alpha=0.75)
#plot(z,w_no_err[:,0],color='gray',ls='--',lw=2,alpha=0.75)
#plot(z,w_no_err[:,2],color='gray',ls='-',lw=2,alpha=0.25)
#plot(z,w_no_err[:,3],color='gray',ls='-',lw=2,alpha=0.25)

ax.hlines(-1,xmin=0,xmax=zmax,linestyles='--',colors='b',lw=2,label=r'Fiducial $w=-1$')


ax.set_xlim(-0.025,zmax+0.025)
ax.set_ylim(-2.05,0.05)

ax.set_xlabel(r'$z$',fontsize=13)
ax.set_ylabel(r'$w(z)$',fontsize=13)
lgd=ax.legend(loc='upper left',frameon=False,fontsize=13)
texts = lgd.get_texts()
setp(texts[0],fontsize=14,color='r')
setp(texts[1],fontsize=14,color='gray')
setp(texts[2],fontsize=14,color='b')

dx = 0.1
dy = 1.1
chisq_val = ' %7.2f'%(chisq_wzCDM-chisq_lcdm)
ax.text(1.5+dx,-1.4+dy,r'$\Delta \chi^2_{\rm data}$',fontsize=15)
ax.text(1.85+dx,-1.4+dy,r'$=$',fontsize=15)
ax.text(1.9+dx,-1.4+dy,chisq_val,fontsize=15)

chisq_val = ' %7.2f'%(chisq_prior+chisq_wzCDM-chisq_lcdm)
ax.text(1.2+dx,-1.6+dy,r'$\Delta \chi^2_{\rm data} + \chi^2_{\rm prior}$',fontsize=15)
ax.text(1.85+dx,-1.6+dy,r'$=$',fontsize=15)
ax.text(1.9+dx,-1.6+dy,chisq_val,fontsize=15)

#ax.text(1.5,-0.055+dy,r'KS-test $p$-values:',fontsize=14)
#ax.text(1.5,-0.2+dy,p_all+' (All)',fontsize=14)
#ax.text(1.5,-0.375+dy,p_sn+' (SNe)',fontsize=14)

ax.text(0.15,-1.855,r'KS-test $p$-values:',fontsize=14)
ax.text(0.15,-2.0,p_all+' (All)',fontsize=14)
ax.text(0.15,-2.175,p_sn+' (SNe)',fontsize=14)

xticks = [0,0.5,1,1.5,2,2.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)

yticks = [-2.5,-2,-1.5,-1,-0.5,0,0.5]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)

ax.tick_params(axis='both',direction='in')

fig.subplots_adjust(top=0.995,bottom=0.1,left=0.125,right=0.975)

fig.savefig('example_w_result_id_80.pdf')


show()
