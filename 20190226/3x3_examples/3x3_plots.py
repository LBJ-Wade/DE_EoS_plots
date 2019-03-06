import sys
from pylab import *

zmax=2.5
amin=1/(1+zmax)
a = linspace(1,amin,30)
z = 1/a-1

colors=['r','g']

EoS_dir = 'post/EoS'
EoS_inv_dir = 'post_inv_err/EoS'

fig = figure(figsize=(10,6))

N1 = 3   # num of rows
N2 = 3  #  num of cols

ids = [9,12,14,28,54,78,89,90,36]

I = 0

dz = 0.005

cnt = 1
for i in range(N1):
    for j in range(N2):
        ax = fig.add_subplot(N1,N2,cnt)
        ax.tick_params(axis='both',direction='in')

        w = loadtxt(EoS_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        # ax.errorbar(z,w[:,0],yerr=[w[:,0]-w[:,2],w[:,3]-w[:,0]],capsize=2,color=colors[0],alpha=0.85)
        ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[0],alpha=0.25)
        ax.plot(z,w[:,0],color=colors[0],ls='-',alpha=0.75)
        ax.plot(z,w[:,2],color=colors[0],ls='-',alpha=0.75)
        ax.plot(z,w[:,3],color=colors[0],ls='-',alpha=0.75)

        w = loadtxt(EoS_inv_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        # ax.errorbar(z+dz,w[:,0],yerr=[w[:,0]-w[:,2],w[:,3]-w[:,0]],capsize=2,color=colors[1],alpha=0.65)
        ax.fill_between(z,y1=w[:,2],y2=w[:,3],color=colors[1],alpha=0.25)
        ax.plot(z,w[:,0],color=colors[1],ls='--',alpha=0.75)
        ax.plot(z,w[:,2],color=colors[1],ls='--',alpha=0.75)
        ax.plot(z,w[:,3],color=colors[1],ls='--',alpha=0.75)

        ax.hlines(-1,xmin=0,xmax=zmax,linestyles='dashed',linewidth=1)
        ax.set_ylim(-2.15,0.15)

        ax.text(0.1,-2,'ID: '+str(ids[cnt-1]))
        # ax.text(0.1,-2,'ID: '+str(cnt))

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
        
        # if cnt == 1:
        #     # lgd=ax.legend(loc='lower left',frameon=False)
        #     # texts = lgd.get_texts()
        #     # for k in range(len(texts)):
        #     #     plt.setp(texts[k],fontsize=8,color=colors[k])
        #     ax.text(0.025,-2.75,'Original result',color=colors[0])
        #     ax.text(0.025,-3.25,'Error inverted',color=colors[1])

        cnt += 1

fig.subplots_adjust(wspace=0,hspace=0,bottom=0.075,top=0.995,left=0.065,right=0.995)
# fig.subplots_adjust(wspace=0,hspace=0,top=0.995,left=0.05,right=0.995)

fig.savefig('examples_3x3.pdf')

show()
