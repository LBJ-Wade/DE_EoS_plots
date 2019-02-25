import sys
from pylab import *

if len(sys.argv) < 2:
    print('usage: %s eos_1.txt eos_2.txt ...')
    sys.exit(0)

w = []
for i in range(1,len(sys.argv)):
    tmp = loadtxt(sys.argv[i])
    w.append(tmp)

a = linspace(1,.4,20)
z = 1/a-1

for i in range(len(w)):
    errorbar(z,w[i][:,0],yerr=w[i][:,1],capsize=2)


show()
