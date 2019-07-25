from pylab import *

n_cross = loadtxt('cross_times_forecast_sigmas.txt')

idx_good = n_cross[:,0] <= 0
idx_bad1 = n_cross[:,0] >= 1
idx_bad2 = n_cross[:,1] >= 1

### do not forget to remove idx_bad2 from idx_bad1

idx_bad1_tmp = idx_bad1

for i in range(len(idx_bad1)):
	if idx_bad2[i] == True:
		idx_bad1_tmp[i] = False

idx_bad1 = idx_bad1_tmp


print('sum(idx_good) = ', sum(idx_good))
print('sum(idx_bad1) = ', sum(idx_bad1))
print('sum(idx_bad2) = ', sum(idx_bad2))

#p = loadtxt('p_all.txt')

chi2_lcdm = loadtxt('chisq_lcdm_forecast.txt')
chi2_dde  = loadtxt('chisq_dde_forecast.txt')
chi2_tot  = chi2_dde[:,0]
dchi2_tot = chi2_dde[:,0]-chi2_lcdm
dchi2_data = chi2_dde[:,2]-chi2_lcdm

chi2_lcdm_ = loadtxt('combined_chisq_lcdm_updated.txt')
chi2_ = loadtxt('combined_chisq.txt')
chi2_tot_ = chi2_[:,0]
chi2_prior_ = chi2_[:,1]
chi2_data_  = chi2_[:,2]
dchi2_tot_jd16 = chi2_[:,0]-chi2_lcdm_[:,0]
dchi2_data_jd16 = chi2_[:,0]-chi2_lcdm_[:,0]-chi2_[:,4]

fig = figure(figsize=(9,5))

colors=['b','grey','g']


nullfmt = NullFormatter()

left    = 0.085
bottom  = 0.115
width   = 0.4
height  = 0.29

_ax_rect1 = [left,bottom+height*2,width,height]
_ax_rect2 = [left,bottom+height*1,width,height]
_ax_rect3 = [left,bottom+height*0,width,height]

dx = 0.035
width_ = 0.465
height_= 3*height
_ax_hist = [left+width+dx, bottom, width_, height_]


ax_rect1 = axes(_ax_rect1)
ax_rect2 = axes(_ax_rect2)
ax_rect3 = axes(_ax_rect3)

ax_hist  = axes(_ax_hist)

# no labels
ax_rect1.xaxis.set_major_formatter(nullfmt)
ax_rect2.xaxis.set_major_formatter(nullfmt)
#ax_rect3.xaxis.set_major_formatter(nullfmt)

############################################################
# plot the randomly selected EoS examples
zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,29)
a = list(a)
a.append(1/1101)
a = array(a)
z = 1/a-1

EoS_dir = 'post_process_piecewise-const/EoS'
EoS_dir2 = 'post_process_forecast/EoS'

ids = []
I=0
N_TOT = 100
while I < 3:
    tmp = randint(1,N_TOT+1)
    if ids.count(tmp) == 0:
        ids.append(tmp)
        I += 1

#ids = [98,10,71]
ids = [26,61,2]
print('IDS: ',ids)

w = loadtxt(EoS_dir+'/eos_'+str(ids[0])+'.txt')
w2 = loadtxt(EoS_dir2+'/eos_'+str(ids[0])+'.txt')

ax_rect1.fill_between(z,y1=w2[:,0]-w2[:,1],y2=w2[:,0]+w2[:,1],color=colors[0],alpha=0.4,label=r'${\rm \Lambda JDF^{\ast}}$')
ax_rect1.plot(z,w2[:,0],color=colors[0],ls='-',alpha=0.35)
ax_rect1.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[1],alpha=0.4,label=r'$\Lambda$'+r'JD16$^{\ast}$')
ax_rect1.plot(z,w[:,0],color=colors[1],ls='--',alpha=0.35)

ax_rect1.hlines(-1,xmin=0,xmax=2.5,linestyles='dashed',colors='k')
ax_rect1.set_xlim(0,2.5)
ax_rect1.set_ylim(-2.15,0.15)
ax_rect1.set_ylabel(r'$w(z)$',fontsize=12)
#lgd = ax_rect1.legend(loc='upper left',ncol=2,bbox_to_anchor=(0.02, 0.975, 2, 0.1),frameon=False)
lgd = ax_rect1.legend(loc='upper left',ncol=2,bbox_to_anchor=(0.02, 1),frameon=False)
txt = lgd.get_texts()
setp(txt[0],color=colors[0],fontsize=12)
setp(txt[1],color=colors[1],fontsize=12)

#ax_rect1.text(0.1,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot[ids[0]],2))+' ',fontsize=12,color=colors[0])
#ax_rect1.text(0.925,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot_jd16[ids[0]],2)),fontsize=12,color=colors[1])
ax_rect1.text(0.1,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data[ids[0]],2))+' ',fontsize=12,color=colors[0])
ax_rect1.text(0.925,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data_jd16[ids[0]],2)),fontsize=12,color=colors[1])
#---------------------------------------------------------------

w = loadtxt(EoS_dir+'/eos_'+str(ids[1])+'.txt')
w2 = loadtxt(EoS_dir2+'/eos_'+str(ids[1])+'.txt')
ax_rect2.fill_between(z,y1=w2[:,0]-w2[:,1],y2=w2[:,0]+w2[:,1],color=colors[0],alpha=0.4,label='Future constraints')
ax_rect2.plot(z,w2[:,0],color=colors[0],ls='-',alpha=0.35)
ax_rect2.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[1],alpha=0.4,label=r'$\Lambda$'+r'JD16$^{\ast}$')
ax_rect2.plot(z,w[:,0],color=colors[1],ls='--',alpha=0.35)

ax_rect2.hlines(-1,xmin=0,xmax=2.5,linestyles='dashed',colors='k')
ax_rect2.set_xlim(0,2.5)
ax_rect2.set_ylim(-2.15,0.15)
ax_rect2.set_ylabel(r'$w(z)$',fontsize=12)

#ax_rect2.text(0.1,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot[ids[1]],2))+' ',fontsize=12,color=colors[0])
#ax_rect2.text(0.925,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot_jd16[ids[1]],2)),fontsize=12,color=colors[1])
ax_rect2.text(0.1,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data[ids[1]],2))+' ',fontsize=12,color=colors[0])
ax_rect2.text(0.925,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data_jd16[ids[1]],2)),fontsize=12,color=colors[1])
#---------------------------------------------------------------

w = loadtxt(EoS_dir+'/eos_'+str(ids[2])+'.txt')
w2 = loadtxt(EoS_dir2+'/eos_'+str(ids[2])+'.txt')
ax_rect3.fill_between(z,y1=w2[:,0]-w2[:,1],y2=w2[:,0]+w2[:,1],color=colors[0],alpha=0.4,label='Future constraints')
ax_rect3.plot(z,w2[:,0],color=colors[0],ls='-',alpha=0.35)
ax_rect3.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[1],alpha=0.4,label=r'$\Lambda$'+r'JD16$^{\ast}$')
ax_rect3.plot(z,w[:,0],color=colors[1],ls='--',alpha=0.35)

ax_rect3.hlines(-1,xmin=0,xmax=2.5,linestyles='dashed',colors='k')
ax_rect3.set_xlim(0,2.5)
ax_rect3.set_ylim(-2.15,0.15)
ax_rect3.set_xlabel(r'$z$',fontsize=12)
ax_rect3.set_ylabel(r'$w(z)$',fontsize=12)

#ax_rect3.text(0.1,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot[ids[2]],2))+' ',fontsize=12,color=colors[0])
#ax_rect3.text(0.925,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchi2_tot_jd16[ids[2]],2)),fontsize=12,color=colors[1])
ax_rect3.text(0.1,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data[ids[2]],2))+' ',fontsize=12,color=colors[0])
ax_rect3.text(0.925,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(dchi2_data_jd16[ids[2]],2)),fontsize=12,color=colors[1])
#---------------------------------------------------------------

############################################################
# plot the histogram of \Delta\chi^2_{\rm tot}
bins=30
alpha=0.65
dchi2_data_stack = []
dchi2_data_stack.append(dchi2_data[idx_good])
dchi2_data_stack.append(dchi2_data[idx_bad1])
dchi2_data_stack.append(dchi2_data[idx_bad2])
colors = ['g','b','r']
labels=[r'Weak-wiggle group', r'Moderate-wiggle group', r'Strong-wiggle group']
n,b,p=ax_hist.hist(dchi2_data_stack,bins=bins,histtype='bar',color=colors,stacked=True,alpha=alpha,label=labels)
ax_hist.set_yticks([])
ax_hist.set_xlabel(r'$\Delta\chi^2_{\rm data}$',fontsize=12)
#ax_hist.set_xlim(-22.5,0.5)
nn =max(n[0].max(),n[1].max(),n[2].max())
ax_hist.set_ylim(0,nn*1.05)
# lgd = ax_hist.legend(loc='upper left',title=r'Deviations from $w=-1$',frameon=False,title_fontsize=13)
lgd = ax_hist.legend(loc='upper left',frameon=False)
txt = lgd.get_texts()
setp(txt[0],fontsize=12,color=colors[0])
setp(txt[1],fontsize=12,color=colors[1])
setp(txt[2],fontsize=12,color=colors[2])

############################################################

fig.savefig('example_chi2_data_forecast.pdf')

show()
