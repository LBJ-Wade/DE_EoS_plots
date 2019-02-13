import numpy as np
from scipy.stats import kstest
from scipy.integrate import quad
from ReadMock import *

# load data
sn_file = 'mock_JLA_20190204/MOCK_JLA_97.txt'
sn = read_jla_mock(sn_file)
dmu = (sn[:,1]-sn[:,3])/sn[:,2]
s,p = kstest(dmu,'norm')

# sample size
n = len(dmu)

# make bins using histogram

hist, bin_edegs = histogram(dmu,bins=50)

# compute theoretically expected numbers in each bins
r = np.zeros(len(hist))

def norm_dist(x):
	return np.exp(-0.5*x**2) / (2*np.pi)**0.5

for i in range(len(hist)):
	a = bin_edegs[i]
	b = bin_edegs[i+1]
	r[i] = quad(norm_dist,a,b)[0]

# compute chi2

chi2 = 0

for i in range(len(hist)):
	chi2 += (hist[i] - n*r[i])**2 / (n*r[i])

print('chi2 = %g'%(chi2))




