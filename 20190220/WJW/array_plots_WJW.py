import sys
from pylab import *

zmax=1.7
amin=1/(1+zmax)
a = linspace(1,amin,20)
z = 1/a-1

EoS_dir = 'EoS_ref_sm_0.04'
EoS_dir_inv_err = 'EoS_sm_0.04_inv_err'

colors=['r','b']
alpha=0.8

fig = figure(figsize=(9,6))
# fig = figure(figsize=(11,7))

N_TOT =100
N1 = 5   # num of rows
N2 = 4  #  num of cols

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

        w = loadtxt(EoS_dir+'/eos_'+str(ids[cnt-1])+'.txt')
        ax.errorbar(z-dz,w[:,0],yerr=w[:,1],capsize=2,color=colors[0],alpha=alpha)

        w = loadtxt(EoS_dir_inv_err+'/eos_'+str(ids[cnt-1])+'.txt')
        ax.errorbar(z+dz,w[:,0],yerr=w[:,1],capsize=2,color=colors[1],alpha=alpha)

        ax.hlines(-1,xmin=0,xmax=zmax,linestyles='dashed',linewidth=1)
        ax.set_xlim(0-10*dz,zmax+dz*10)
        ax.set_ylim(-3.25,0.5)

        # ax.text(0.025,0,'ID='+str(ids[cnt-1]))

        if i == N1-1:
            ax.set_xticks([0,0.5,1.0,1.5])
            ax.set_xticklabels([0,0.5,1.0,1.5],fontsize=8,rotation=0)
            ax.set_xlabel('z')
        else:
            ax.set_xticklabels('')
        if j > 0:
            ax.set_yticklabels('')
        else:
            yticks = [-3,-2,-1,0]
            ax.set_yticks(yticks)
            ax.set_yticklabels(yticks,fontsize=8)
            ax.set_ylabel(r'$w(z)$')
        
        if cnt == 1:
            ax.text(0.025,-2.25,'Original result',color=colors[0])
            ax.text(0.025,-2.75,'Error inverted',color=colors[1])

        cnt += 1

# fig.subplots_adjust(wspace=0.,hspace=0,bottom=0.075,top=0.995,left=0.075,right=0.995)
fig.subplots_adjust(wspace=0.,hspace=0,bottom=0.075,top=0.995,left=0.05,right=0.995)

fig.savefig('EoS_list_WJW.pdf')

show()
