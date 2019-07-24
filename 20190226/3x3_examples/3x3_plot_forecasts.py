import sys
from pylab import *

#zmax=2.5
#amin=1/(1+zmax)
#a = linspace(1,amin,30)
#z = 1/a-1

zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,29)
a = list(a)
a.append(1/1101)
a = array(a)
z = 1/a-1

colors=['r','b','g']

chisq_lcdm = loadtxt('post_process_forecast_LCDM/chisq_lcdm.txt')
chisq = loadtxt('post_process_forecast/chisq.txt')

EoS_dir = 'post_process_piecewise-const/EoS'
EoS_dir2 = 'post_process_forecast/EoS'

fig = figure(figsize=(10,6.5))

N1 = 3   # num of rows
N2 = 3  #  num of cols

# ids = [9,12,14,28,54,78,89,90,36]

ids0 = loadtxt('ids_good.txt',dtype=int)
ids1 = loadtxt('ids_1sigma.txt',dtype=int)
ids2 = loadtxt('ids_2sigma.txt',dtype=int)

chi2_lcdm = loadtxt('chisq_lcdm_forecast.txt')
chi2_dde  = loadtxt('chisq_dde_forecast.txt')
chi2_tot  = chi2_dde[:,0]
dchi2_tot = chi2_dde[:,0]-chi2_lcdm
dchi2_dat = chi2_dde[:,2]-chi2_lcdm

n_cross = loadtxt('cross_times_forecast.txt')

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


ids = []


I=0
N_TOT = 100
while I < N1*N2:
    tmp = randint(1,N_TOT+1)
    if ids.count(tmp) == 0:
        ids.append(tmp)
        I += 1

cnt = 1
for i in range(N1):
    for j in range(N2):
        ax = fig.add_subplot(N1,N2,cnt)
        ax.tick_params(axis='both',direction='in')

        if cnt < 9:
            idx = ids[cnt-1]-1
            
            chisq_lcdm_tmp = chisq_lcdm[idx]
            chisq_tot_tmp = chisq[idx,0]
            chisq_data_tmp= chisq[idx,2]

            w = loadtxt(EoS_dir+'/eos_'+str(ids[cnt-1])+'.txt')
            ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[0],alpha=0.3,label=r'$\Lambda$'+r'JD16$^{\ast}$')
            ax.plot(z,w[:,0],color=colors[0],ls='--',alpha=0.35)

            w = loadtxt(EoS_dir2+'/eos_'+str(ids[cnt-1])+'.txt')
            ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[1],alpha=0.3,label='Future constraints')
            ax.plot(z,w[:,0],color=colors[1],ls='-',alpha=0.5)

            ax.hlines(-1,xmin=0,xmax=zmax,linestyles='dashed',linewidth=1)
            ax.set_ylim(-2.15,0.15)

            # ax.text(0.1,-2,'ID: '+str(ids[cnt-1]))

            # add Delta chisq
            ax.text(0.1,-2,r'$\Delta\chi^2_{\rm data} = $ ' + str(round(chisq_data_tmp-chisq_lcdm_tmp,3))+', ',fontsize=12,color='k')
            ax.text(1.2,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(chisq_tot_tmp-chisq_lcdm_tmp,3)),fontsize=12,color='k')

            ax.set_xlim(0,2.5)
            if i == N1-1:
                xticks = [0,0.5,1.0,1.5,2]
                ax.set_xticks(xticks)
                ax.set_xticklabels(xticks,fontsize=8)
                ax.set_xlabel('z')
            else:
                ax.set_xticklabels('')
            if j > 0:
                ax.set_yticklabels('')
            else:
                # ax.set_yticks([-3,-2,-1,0])
                # ax.set_yticklabels([-3,-2,-1,0],fontsize=8)
                ax.set_ylabel(r'$w(z)$')
            
            if cnt == 1:
                lgd = ax.legend(loc='upper left',ncol=2,frameon=False)
                txt = lgd.get_texts()
                setp(txt[0],fontsize=10,color='r',alpha=0.75)
                setp(txt[1],fontsize=10,color='b',alpha=0.75)

        else:
            bins=30
            alpha=0.45
            dchi2_tot_stack = []
            dchi2_tot_stack.append(dchi2_tot[idx_good])
            dchi2_tot_stack.append(dchi2_tot[idx_bad1])
            dchi2_tot_stack.append(dchi2_tot[idx_bad2])
            colors = ['g','b','r']
            labels=[r'all $w_i$: $<1\sigma$',r'at least one $w_i$: $\geq 1\sigma$ and $<2\sigma$',r'at least one $w_i$: $\geq 2\sigma$']
#            ax.hist(dchi2_tot,bins=bins,histtype='step')
            n,b,p=ax.hist(dchi2_tot_stack,bins=bins,histtype='bar',color=colors,stacked=True,alpha=alpha,label=labels)
            ax.set_yticks([])
            ax.set_xlabel(r'$\Delta\chi^2_{\rm tot}$',fontsize=12)
            ax.set_xlim(-25,1.25)
            nn =max(n[0].max(),n[1].max(),n[2].max())
            ax.set_ylim(0,nn*1.125)
            lgd = ax.legend(loc='upper left',title=r'Deviations from $w=-1$',frameon=False)
            txt = lgd.get_texts()
            setp(txt[0],fontsize=9,color=colors[0])
            setp(txt[1],fontsize=9,color=colors[1])
            setp(txt[2],fontsize=9,color=colors[2])
            
        cnt += 1

fig.subplots_adjust(wspace=0,hspace=0,bottom=0.075,top=0.995,left=0.065,right=0.995)
# fig.subplots_adjust(wspace=0,hspace=0,top=0.995,left=0.05,right=0.995)

fig.savefig('examples_3x3_forecasts_20190711.pdf')

show()
