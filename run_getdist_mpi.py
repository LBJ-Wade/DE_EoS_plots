import os,sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

chain_root = ''
chain_num = -1

if len(sys.argv) != 3:
	if rank == 0:
		print('> usage: %s chain_root chain_num'%(sys.argv[0]))
	sys.exit(0)
else:
	chain_root = sys.argv[1]
	chain_num  = int(sys.argv[2])

# root rank check the existence of directory 'results'
if rank == 0:
	if os.path.isdir('results'):
		print "the directory \'results\' is already there"
	else:
		os.system("mkdir results")
	
	if os.path.isdir('tmp') is False:
		os.system("mkdir tmp")

# make sure results and tmp are there
comm.Barrier()


n_start = 1
n_end = 0
n_all = 0

n_tot = chain_num

n_all = n_tot / size

n_start = rank*n_all + 1

if rank == size-1:
	n_all_tmp = n_all
	n_all += (n_tot-n_all*size)

#chain_root='WJW_sm_0.08_inv_err'

for n in range(n_start,n_start+n_all):
	CMD=""
	CMD += "m4 -DKEY_FILE_ROOT=\'file_root = " + chain_root + "_" + str(n)+"/EoS_SN_CMB\'"
	CMD += " -DKEY_OUT_ROOT=\'out_root = results/EoS_"+str(n)+"\' "
	CMD += " GetDist.ini > tmp/dist_"+str(n)+".ini\n"
#	CMD += " getdist tmp/dist_"+str(n)+".ini"

	os.system(CMD)

	dist_file = 'tmp/dist_'+str(n)+'.ini'
	if os.path.isfile(dist_file):
		os.system("getdist "+dist_file)
	else:
		print 'rank: %2d, cannot find getdist ini file: %s'%(rank,dist_file)

comm.Barrier()


#if rank == 0:
#	for i in range(1,1001):
#		fname = 'tmp/dist_'+str(i)+'.ini'
#		if os.path.isfile(fname):
#			print 'found %s'%(fname)
#		else:
#			print 'cannot find %s'%(fname)


#if rank == 0 :
#	os.system("rm -r tmp")

