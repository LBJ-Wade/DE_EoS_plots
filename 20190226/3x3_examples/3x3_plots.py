import sys
from pylab import *

colors=['r','b','g']

zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,29)
a = list(a)
a.append(1/1101)
a = array(a)
z = 1/a-1
#######################################################

# number of {w_i} crosses w=-1
ct = loadtxt('cross_times_sigmas.txt')

# bestfit chisq for LCDM and DDE-model
chisq_lcdm = loadtxt('combined_chisq_lcdm_updated.txt')
chisq = loadtxt('combined_chisq.txt')

# folders that store the EOS results
EoS_dir = 'post_process_piecewise-const/EoS'
EoS_inv_dir = 'post_process_piecewise-const-inv-err/EoS'


fig = figure(figsize=(10,7))

N1 = 3  # num of rows
N2 = 3  # num of cols

#######################################################
ids = []

N_TOT = 100
I = 0
while I < N1*N2:
    tmp = randint(1,N_TOT+1)
    if ids.count(tmp) == 0 and tmp != 80:
        ids.append(tmp)
        I += 1

#######################################################

ids = loadtxt('used_ids-xx.txt',dtype=int)

print(ids)
#savetxt('used_ids.txt',ids,fmt='%3d')
#print(ct[ids,0])


# sort ids[] according to values of \Delta\chi^2_{tot}
#dchisq_tot = chisq[ids,0] - chisq_lcdm[ids,0]
#dchisq_dat = (chisq[ids,0]-chisq[ids,4])-chisq_lcdm[ids,0]

dchisq_tot = []
dchisq_dat = []

for i in range(len(ids)):
    dchisq_tot.append(chisq[ids[i]-1,0]-chisq_lcdm[ids[i]-1,0])
    dchisq_dat.append((chisq[ids[i]-1,0]-chisq[ids[i]-1,4])-chisq_lcdm[ids[i]-1,0])

dchisq_tot = array(dchisq_tot)
dchisq_dat = array(dchisq_dat)

ids_sorted = dchisq_tot.argsort()

for i in range(len(ids)):
	j = ids_sorted[i]
	id_tmp = ids[j]
	print('corss times of EoS_%2d is: %3d, dchisq_tot = %10.6f, dchisq_dat = %10.6f'%(id_tmp,ct[id_tmp-1,0],dchisq_tot[j],dchisq_dat[j]))

cnt = 1
for i in range(N1):
    for j in range(N2):
        ax = fig.add_subplot(N1,N2,cnt)
        ax.tick_params(axis='both',direction='in')
        
#        idx = ids[cnt-1]-1
        k = ids_sorted[cnt-1]
        idx = ids[k]
        
        print('==> idx = %5d'%(idx))
        
        chisq_lcdm_tmp = chisq_lcdm[idx-1,0]
        chisq_tot_tmp = chisq[idx-1,0]
        chisq_data_tmp= chisq[idx-1,0] - chisq[idx-1,4]

#        w = loadtxt(EoS_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        w = loadtxt(EoS_dir+'/eos_'+str(idx)+'.txt')
        ax.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[0],alpha=0.25,label=r'${\rm \Lambda JD16^{\ast}}$')
        ax.plot(z,w[:,0],color=colors[0],ls='-',alpha=0.75)
        ax.plot(z,w[:,0]-w[:,1],color=colors[0],ls='-',alpha=0.75)
        ax.plot(z,w[:,0]+w[:,1],color=colors[0],ls='-',alpha=0.75)

#        w = loadtxt(EoS_inv_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        w = loadtxt(EoS_inv_dir+'/eos_'+str(idx)+'.txt')
        ax.fill_between(z,y1=w[:,0]-w[:,1],y2=w[:,0]+w[:,1],color=colors[1],alpha=0.25,label=r'${\rm \Lambda JD16^{\ast}}$ with errors inverted')
        ax.plot(z,w[:,0],color=colors[1],ls='-',lw=1,alpha=0.75)
        ax.plot(z,w[:,0]-w[:,1],color=colors[1],ls='--',alpha=0.75)
        ax.plot(z,w[:,0]+w[:,1],color=colors[1],ls='--',alpha=0.75)

        if cnt == 1:
            # lgd = ax.legend(loc='upper right',frameon=False)
            # txt = lgd.get_texts()
            # setp(txt[0],fontsize=12,color='b',alpha=0.75)
            labels=[r'${\rm \Lambda JD16^{\ast}}$',r'${\rm \Lambda JD16^{\ast}}$ with errors inverted']
            # lgd=ax.legend(loc='upper center',ncol=2,bbox_to_anchor=(1.5, 1.25),labels=labels,frameon=False)
            lgd=ax.legend(loc='upper center',ncol=2,bbox_to_anchor=(1.5, 1.25),frameon=False)
            txt = lgd.get_texts()
            setp(txt[0],fontsize=12,color=colors[0])
            setp(txt[1],fontsize=12,color=colors[1])
        	
        ax.hlines(-1,xmin=0,xmax=zmax,linestyles='dashed',linewidth=1)
        ax.set_ylim(-2.15,0.15)

#        ax.text(0.1,-1.65,'ID: '+str(ids[cnt-1]))
#        ax.text(0.1,-1.65,'ID: '+str(idx))
        # ax.text(0.1,-2,'ID: '+str(cnt))
        
        # add Delta chisq
#        ax.text(0.1,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(chisq_tot_tmp-chisq_lcdm_tmp,2)),fontsize=12,color='k')
        ax.text(0.1,-2,r'$\Delta\chi^2_{\rm tot} = $ ' + str(round(dchisq_tot[k],2)),fontsize=12,color='k')

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
        
        cnt += 1

fig.subplots_adjust(wspace=0,hspace=0,bottom=0.075,top=0.925,left=0.065,right=0.995)
# fig.subplots_adjust(wspace=0,hspace=0,top=0.995,left=0.05,right=0.995)

#fig.savefig('examples_3x3.pdf')

show()
