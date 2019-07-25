from pylab import *

w = loadtxt('post_process_piecewise-const/EoS/eos_80.txt')

EoS_no_err_dir = 'post_no_err_sm_0.04/EoS'
w_no_err = loadtxt(EoS_no_err_dir+'/eos_1.txt')
w_peak = loadtxt(EoS_no_err_dir+'/EoS_1_w_peak_vals.txt')


p_all= '0.58'
p_sn = '0.59'

#chisq_prior = 8.34348
#chisq_wzCDM = 838.823-chisq_prior
#chisq_lcdm = 841.459656

chisq_prior = 1.47187
chisq_wzCDM = 830.708-chisq_prior
#chisq_lcdm = 841.459656
chisq_lcdm = 836.303191

zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,29)
a = list(a)
a.append(1/1101)
a = array(a)
z = 1/a-1

fig = figure(figsize=(6,5))

ax = fig.add_subplot(1,1,1)

ax.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color='r',alpha=0.3,label=r'$\rm{\Lambda JD16^{\ast}}$')
ax.plot(z,w[:,0],ls='-',color='r',lw=3)
ax.plot(z,w[:,0]-w[:,1],ls='-',color='r',lw=2,alpha=0.75)
ax.plot(z,w[:,0]+w[:,1],ls='-',color='r',lw=2,alpha=0.75)

#ax.fill_between(z,y1=w_no_err[:,2],y2=w_no_err[:,3],color='gray',alpha=0.25,label=r'$\rm{\Lambda JD16^{\ast}}$ with $d=d^{\rm th}$')
# ax.fill_between(z,y1=w_no_err[:,0]-w_no_err[:,1],y2=w_no_err[:,0]+w_no_err[:,1],color='gray',alpha=0.25,label=r'$\rm{\Lambda JD16^{\ast}}$ with $\mathbf{d}=\mathbf{d}^{\rm th}$')
ax.fill_between(z,y1=w_peak-w_no_err[:,1],y2=w_peak+w_no_err[:,1],color='gray',alpha=0.25,label=r'$\rm{\Lambda JD16^{\ast}}$ with $\mathbf{d}=\mathbf{d}^{\rm th}$')
plot(z,w_peak,color='gray',ls='-.',lw=2,alpha=0.5)
# plot(z,w_no_err[:,0],color='gray',ls='--',lw=2,alpha=0.5)
#plot(z,w_no_err[:,2],color='gray',ls='-',lw=2,alpha=0.25)
#plot(z,w_no_err[:,3],color='gray',ls='-',lw=2,alpha=0.25)

ax.hlines(-1,xmin=0,xmax=zmax,linestyles='--',colors='k',lw=2)


ax.set_xlim(0,zmax)
ax.set_ylim(-2,0)

ax.set_xlabel(r'$z$',fontsize=13)
ax.set_ylabel(r'$w(z)$',fontsize=13)
lgd=ax.legend(loc='upper left',frameon=False,fontsize=13)
texts = lgd.get_texts()
setp(texts[0],fontsize=14,color='r')
setp(texts[1],fontsize=14,color='gray')
#setp(texts[2],fontsize=14,color='k')

dx = -1.3
dy = -0.5
chisq_val = ' %7.2f'%(chisq_wzCDM-chisq_lcdm)
ax.text(1.5+dx,-1.4+dy,r'$\Delta \chi^2_{\rm data}$',fontsize=15)
ax.text(1.85+dx,-1.4+dy,r'$=$',fontsize=15)
ax.text(1.9+dx,-1.4+dy,chisq_val,fontsize=15)

#chisq_val = ' %7.2f'%(chisq_prior+chisq_wzCDM-chisq_lcdm)
#ax.text(1.5+dx,-1.6+dy,r'$\Delta \chi^2_{\rm tot}$',fontsize=15)
#ax.text(1.85+dx,-1.6+dy,r'$=$',fontsize=15)
#ax.text(1.9+dx,-1.6+dy,chisq_val,fontsize=15)


#ax.text(0.15,-2.0,p_all+' (All)',fontsize=14)
#ax.text(0.15,-2.175,p_sn+' (SNe)',fontsize=14)

xticks = [0,0.5,1,1.5,2,2.5]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks,fontsize=13)

yticks = [-2.5,-2,-1.5,-1,-0.5,0,0.5]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks,fontsize=13)

ax.tick_params(axis='both',direction='in')

fig.subplots_adjust(top=0.985,bottom=0.1,left=0.125,right=0.975)

#fig.savefig('example_w_result_id_80_0604.pdf')
fig.savefig('example_w_result_dat.pdf')


show()
