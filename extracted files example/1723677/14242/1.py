import cudf, cupy, math, warnings, time 
from numba import cuda, float32, int8
import numpy as np, pandas as pd, os, gc
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

LOCAL_VALIDATION = False

# LIST COLUMNS TO LOAD
cols = ['TransactionID', 'TransactionDT', 'TransactionAmt',
       'ProductCD', 'card1', 'card2', 'card3', 'card4', 'card5', 'card6',
       'addr1', 'addr2', 'dist1', 'dist2', 'P_emaildomain', 'R_emaildomain',
       'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
       'C12', 'C13', 'C14', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
       'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'M1', 'M2', 'M3', 'M4',
       'M5', 'M6', 'M7', 'M8', 'M9']
# USEFUL V COLUMNS
v =  [1, 3, 4, 6, 8, 11]
v += [13, 14, 17, 20, 23, 26, 27, 30]
v += [36, 37, 40, 41, 44, 47, 48]
v += [54, 56, 59, 62, 65, 67, 68, 70]
v += [76, 78, 80, 82, 86, 88, 89, 91]
v += [107, 108, 111, 115, 117, 120, 121, 123] 
v += [124, 127, 129, 130, 136] 
v += [138, 139, 142, 147, 156, 162] 
v += [165, 160, 166] 
v += [178, 176, 173, 182] 
v += [187, 203, 205, 207, 215] 
v += [169, 171, 175, 180, 185, 188, 198, 210, 209] 
v += [218, 223, 224, 226, 228, 229, 235] 
v += [240, 258, 257, 253, 252, 260, 261] 
v += [264, 266, 267, 274, 277] 
v += [220, 221, 234, 238, 250, 271] 
v += [294, 284, 285, 286, 291, 297] 
v += [303, 305, 307, 309, 310, 320] 
v += [281, 283, 289, 296, 301, 314] 
cols += ['V'+str(x) for x in v]

# DECLARE COLUMN DTYPES
dtypes = {'isFraud':'int8'}
for c in cols+['id_0'+str(x) for x in range(1,10)]+['id_'+str(x) for x in range(10,34)]: dtypes[c] = 'float32'
for c in ['id-0'+str(x) for x in range(1,10)]+['id-'+str(x) for x in range(10,34)]: dtypes[c] = 'float32'
str_type = ['ProductCD', 'card4', 'card6', 'P_emaildomain', 'R_emaildomain','M1', 'M2', 'M3', 'M4','M5',
            'M6', 'M7', 'M8', 'M9', 'id_12', 'id_15', 'id_16', 'id_23', 'id_27', 'id_28', 'id_29', 'id_30', 
            'id_31', 'id_33', 'id_34', 'id_35', 'id_36', 'id_37', 'id_38', 'DeviceType', 'DeviceInfo']
str_type += ['id-12', 'id-15', 'id-16', 'id-23', 'id-27', 'id-28', 'id-29', 'id-30', 
            'id-31', 'id-33', 'id-34', 'id-35', 'id-36', 'id-37', 'id-38']
for c in str_type: dtypes[c] = 'category'
#for c in str_type: dtypes[c] = 'str'

start = time.time()
print('RAPIDS =',cudf.__version__)
