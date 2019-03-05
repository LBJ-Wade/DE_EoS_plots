import sys
from pylab import *

zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,30)
z = 1/a-1

colors=['b','g']

EoS_dir = 'EoS_JLA_full_cov'
# EoS_dir = 'EoS_no_cov'

fig = figure(figsize=(12,8))

N_TOT = 50
N1 = 7   # num of rows
N2 = 7  #  num of cols

ids = []

I = 0

while I < N1*N2:
    tmp = randint(1,N_TOT+1)
    if ids.count(tmp) == 0:
        ids.append(tmp)
        I += 1

dz = 0.005

cnt = 1
for i in range(N1):
    for j in range(N2):
        ax = fig.add_subplot(N1,N2,cnt)
        ax.tick_params(axis='both',direction='in')

        # w = loadtxt(EoS_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        w = loadtxt(EoS_dir+'/eos_'+str(cnt)+'.txt')
        # ax.errorbar(z,w[:,0],yerr=w[:,1],capsize=2,color=colors[0],alpha=0.65)
        ax.errorbar(z,w[:,0],yerr=[w[:,0]-w[:,2],w[:,3]-w[:,0]],capsize=2,color=colors[0],alpha=0.85)
        ax.fill_between(z,y1=w[:,2],y2=w[:,3],color='r',alpha=0.25)
        # ax.errorbar(z,-2-w[:,0],yerr=w[:,1],capsize=2,color=colors[0],alpha=0.65)

        # w = loadtxt('EoS_err_inv2/eos_'+str(ids[cnt-1])+'.txt')
        # ax.errorbar(z+dz,w[:,0],yerr=w[:,1],capsize=2,color=colors[1],alpha=0.65)

        ax.hlines(-1,xmin=0,xmax=zmax,linestyles='dashed',linewidth=1)
        ax.set_ylim(-2.5,0.5)

        # ax.text(0.1,-2,'ID: '+str(ids[cnt-1]))
        ax.text(0.1,-2,'ID: '+str(cnt))

        if i == N1-1:
            xticks = [0,0.5,1.0,1.5,2,2.5]
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
        
        # if cnt == 1:
        #     # lgd=ax.legend(loc='lower left',frameon=False)
        #     # texts = lgd.get_texts()
        #     # for k in range(len(texts)):
        #     #     plt.setp(texts[k],fontsize=8,color=colors[k])
        #     ax.text(0.025,-2.75,'Original result',color=colors[0])
        #     ax.text(0.025,-3.25,'Error inverted',color=colors[1])

        cnt += 1

fig.subplots_adjust(wspace=0,hspace=0,bottom=0.1,top=0.995,left=0.05,right=0.995)

# fig.savefig('EoS_list.pdf')

show()
