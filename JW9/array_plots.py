import sys
from pylab import *

zmax=1.5
amin=1/(1+zmax)
a = linspace(1,amin,20)
z = 1/a-1



fig = figure(figsize=(10,7))

N_TOT = 50
N1 = 5   # num of rows
N2 = 4  #  num of cols

ids = []

I = 0

while I < N1*N2:
    tmp = randint(1,N_TOT)
    if ids.count(tmp) == 0:
        ids.append(tmp)
        I += 1

cnt = 1
for i in range(N1):
    for j in range(N2):
        ax = fig.add_subplot(N1,N2,cnt)

        w = loadtxt('EoS_ref/eos_'+str(ids[cnt-1])+'.txt')
        ax.errorbar(z,w[:,0],yerr=w[:,1],capsize=2,label=r'standard')
        
        w = loadtxt('EoS_wider_w_range/eos_'+str(ids[cnt-1])+'.txt')
        ax.errorbar(z,w[:,0],yerr=w[:,1],capsize=2,label=r'wider w range')

        ax.hlines(-1,xmin=0,xmax=1.5,linestyles='dashed',linewidth=1)
        cnt += 1
        ax.set_ylim(-2.5,0.5)
        if i == N1-1:
            ax.set_xticks([0,0.5,1.0,1.5])
            ax.set_xticklabels([0,0.5,1.0,1.5],fontsize=8)
            ax.set_xlabel('z')
        else:
            ax.set_xticklabels('')
        if j > 0:
            ax.set_yticklabels('')
        else:
            ax.set_ylabel(r'$w(z)$')
        ax.legend(loc='best',frameon=False)

fig.subplots_adjust(wspace=0,hspace=0,bottom=0.065,top=0.995,left=0.055,right=0.995)

# fig.savefig('EoS_list.pdf')

show()
