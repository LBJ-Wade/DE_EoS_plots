import sys,os
from pylab import *

def read_jla_mock(snfile):
    jla = []
    fp = open(snfile,'r')
    lines = fp.readlines()
    for l in lines:
        snname,z,mu,mu_std,mu0=l.split()
        sn = []
        sn.append(float(z))
        sn.append(float(mu))
        sn.append(float(mu_std))
        sn.append(float(mu0))
        jla.append(sn)
    fp.close()
    
    return array(jla)

def read_wfirst_mock(snfile):
    wfirst = []
    fp = open(snfile,'r')
    lines = fp.readlines()
    for l in lines:
        z,mu,mu_std,mu0=l.split()
        sn = []
        sn.append(float(z))
        sn.append(float(mu))
        sn.append(float(mu_std))
        sn.append(float(mu0))
        wfirst.append(sn)
    fp.close()
    
    return array(wfirst)