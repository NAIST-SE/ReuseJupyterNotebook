def mean2(x,y_out):
    # ALLOCATE SHARED MEMORY
    sum = cuda.shared.array((2),dtype=float32)
    sum[0] = 0; sum[1] = 0
    cuda.syncthreads()
    # COMPUTE SUM AND SKIP NULL
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        if (x[i]!=-1): cuda.atomic.add(sum,0,x[i])
        else: cuda.atomic.add(sum,1,1)
    cuda.syncthreads()
    # OUTPUT MEAN WITHOUT NULL
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        if (len(x)-sum[1])<=0: y_out[i] = -1
        else: y_out[i] = sum[0]/(len(x)-sum[1])
        
def std2(x,y_out):
    # ALLOCATE SHARED MEMORY
    sum = cuda.shared.array((3),dtype=float32)
    for i in range(3): sum[i] = 0
    cuda.syncthreads()
    # COMPUTE MEAN AND SKIP NULL
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        if (x[i]!=-1): cuda.atomic.add(sum,0,x[i])
        else: cuda.atomic.add(sum,2,1)
    cuda.syncthreads()
    if cuda.threadIdx.x==0: sum[0] = sum[0]/(len(x)-sum[2])
    cuda.syncthreads()
    # COMPUTE SUM OF SQUARES AND SKIP NULL
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        if (x[i]!=-1): cuda.atomic.add(sum,1,(x[i]-sum[0])**2) 
    cuda.syncthreads()
    # OUTPUT STANDARD DEVIATION WITHOUT NULL
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        if (len(x)-sum[2])<=1: y_out[i] = -1
        else: y_out[i] = math.sqrt( sum[1]/(len(x)-sum[2]-1) )
            
def count2(x,y_out):
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):  
        y_out[i] = len(x)
        
def nunique2(x,y_out):
    # ALLOCATE SHARED MEMORY
    record = cuda.shared.array((2048),dtype=int8)
    for i in range(2048): record[i] = 0
    cuda.syncthreads()
    # RECORD UNIQUES
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        record[ int(x[i]*1e6)%2048 ] = 1
    cuda.syncthreads()
    # OUTPUT NUNIQUE
    sum = 0
    for j in range(2048): sum = sum + record[j]
    for i in range(cuda.threadIdx.x,len(x),cuda.blockDim.x):
        y_out[i] = sum
