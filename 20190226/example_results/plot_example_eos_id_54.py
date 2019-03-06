from pylab import *

w = loadtxt('post/EoS/eos_54.txt')
wb = loadtxt('eos_best_fit_id_54.txt')
# p_all= '0.679059'
# p_sn = '0.812967'
p_all= '0.68'
p_sn = '0.81'
chisq_lcdm = 799.052080
chisq_wzCDM= 792.321
chisq_prior= 5.98999

# w = loadtxt('eos_37.txt')
# p = 0.83
# chisq_lcdm = 832.693329
# chisq_wzCDM= 831.013

zmax = 2.5
a = linspace(1,1/(1+zmax),30)
z = 1/a-1

fig = figure(figsize=(6,5))

ax = fig.add_subplot(1,1,1)

ax.fill_between(z,y1=w[:,2],y2=w[:,3],color='r',alpha=0.3,label=r'Reconstructed $w(z)$')
ax.plot(z,w[:,2],ls='-',color='r',lw=2,alpha=0.75)
ax.plot(z,w[:,3],ls='-',color='r',lw=2,alpha=0.75)
ax.plot(z,w[:,0],ls='-',color='r',lw=3,)
# ax.plot(z,wb,'-s',color='r',lw=1,)

ax.hlines(-1,xmin=0,xmax=zmax,linestyles='--',colors='b',lw=2,label=r'Fiducial $w=-1$')


ax.set_xlim(-0.025,zmax+0.025)
ax.set_ylim(-2.15,0.05)

ax.set_xlabel(r'$z$',fontsize=13)
ax.set_ylabel(r'$w(z)$',fontsize=13)
lgd=ax.legend(loc='upper right',frameon=False,fontsize=13)
texts = lgd.get_texts()
setp(texts[0],fontsize=14,color='r')
setp(texts[1],fontsize=14,color='b')

# text(1.5,-1.25,r'$\chi^2_{\rm LCDM} = ' + str(round(chisq_lcdm,3)) + '$',fontsize=14)
# text(1.5,-1.45,r'$\chi^2_{\rm w(z)CDM} = ' + str(round(chisq_wzCDM,3)) + '$',fontsize=14)

dx = -1.15
dy = -0.25
chisq_val = ' %8.3f'%(chisq_wzCDM-chisq_lcdm)
ax.text(1.5+dx,-1.6+dy,r'$\Delta \chi^2_{\rm data}$',fontsize=15)
ax.text(1.85+dx,-1.6+dy,r'$=$',fontsize=15)
ax.text(1.9+dx,-1.6+dy,chisq_val,fontsize=15)

chisq_val = ' %8.3f'%(chisq_prior+chisq_wzCDM-chisq_lcdm)
ax.text(1.2+dx,-1.8+dy,r'$\Delta \chi^2_{\rm data} + \chi^2_{\rm prior}$',fontsize=15)
ax.text(1.85+dx,-1.8+dy,r'$=$',fontsize=15)
ax.text(1.9+dx,-1.8+dy,chisq_val,fontsize=15)

ax.text(1.3,-0.2+dy*2,r'$p$-value = '+p_all+' (All)',fontsize=14)
ax.text(1.3,-0.35+dy*2,r'$p$-value = '+p_sn+' (SNe)',fontsize=14)

xticks = [0,0.5,1,1.5,2,2.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)

yticks = [-2,-1.5,-1,-0.5,0]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)

fig.subplots_adjust(top=0.995,bottom=0.1,left=0.125,right=0.975)

fig.savefig('example_w_result_id_54.pdf')

# plot BAO and SN fitting

# ax = fig.add_subplot()



show()