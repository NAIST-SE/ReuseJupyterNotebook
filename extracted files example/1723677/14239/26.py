import numpy as np
np.random.seed(42)
x = np.random.choice(np.arange(30),2)
print('We will submit versions',x[0],'and',x[1])
np.random.seed(None)
