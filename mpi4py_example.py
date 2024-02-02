## LKD 23-02-2023 MPI MWE                                                                                                                                    
import mpi4py                                                                                                                                                                                                      
mpi4py.rc.initialize = False                                                                                                                                                                                       
mpi4py.rc.finalize = False                                                                                                                                                                                                                                                                                                                                                                                   
from mpi4py import MPI                                                                                                                                            
import time                                                                                                                                                  

MPI.Init()
# initialize the MPI threads                                                                                                                                 
comm = MPI.COMM_WORLD                                                                                                                                        
                                                                                                                                                             
# grab # of processes (it will match 'mpirun -n <nprocs> <exe>'                                                                                              
nprocs = comm.Get_size()                                                                                                                                     
                                                                                                                                                             
# tell a thread it's rank (it's like an ID number for each thread which we can use to execute parallel code)                                                 
rank = comm.Get_rank()                                                                                                                                       
                                                                                                                                                             
# master thread starts their clock (rank==0 will be only one when run in serial i.e. mpirun -n 1 ...)                                                        
if rank==0:                                                                                                                                                  
    start_time = time.time()                                                                                                                                 
                                                                                                                                                             
# let's do a basic for loop playing with real numbers                                                                                                        
xmin = 0.0                                                                                                                                                   
xmax = 128.0                                                                                                                                                 
xdelta = 1.0                                                                                                                                                 
                                                                                                                                                             
# chunksize for each processor                                                                                                                               
rank_x_split = (xmax-xmin)/float(nprocs)                                                                                                                     
                                                                                                                                                             
rank_xmax = rank_x_split*float(rank + 1) + xmin                                                                                                              
rank_xbegin = rank_x_split*float(rank)+ xmin                                                                                                                 
                                                                                                                                                             
# each thread has a unique list now                                                                                                                          
xs = np.arange(rank_xbegin,rank_xmax,xdelta)                                                                                                                 
                                                                                                                                                             
for x in xs:                                                                                                                                                 
    time.sleep(0.1)                                                                                                                                          
                                                                                                                                                             
if rank==0:                                                                                                                                                  
    print("--- %s seconds ---" % (time.time() - start_time)) 

MPI.Finalize()
