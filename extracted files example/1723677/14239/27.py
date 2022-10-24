import matplotlib.pyplot as plt, numpy as np
pu = np.array([68,53,70,67,54,54,39,68,60,65,46,62,62,55,54,
               60,59,55,43,52,63,68,51,75,81,56,68,55,60,48])
pr = np.array([58,54,68,54,48,61,59,49,60,57,70,54,53,69,72,
               56,64,44,88,63,74,70,43,48,77,65,51,70,51,48])
plt.scatter(0.974+pu/1e5,0.975+pr/1e5)
plt.scatter(0.974+pu[5]/1e5,0.975+pr[5]/1e5,color='green',s=100)
plt.scatter(0.974+pu[18]/1e5,0.975+pr[18]/1e5,color='green',s=100)

mpu = 0.974 + np.mean(pu)/1e5
mpr = 0.975 + np.mean(pr)/1e5
plt.plot([mpu,mpu],[mpr-0.0005,mpr+0.0005],':k')
plt.plot([mpu-0.0005,mpu+0.0005],[mpr,mpr],':k')

plt.xlabel('Public LB'); plt.xlim((mpu-0.0005,mpu+0.0005))
plt.ylabel('Private LB'); plt.ylim((mpr-0.0005,mpr+0.0005))
plt.title("Public and private LB scores from 30 runs of this kernel.\n \
    The green dots were the two randomly chosen submissions")
plt.show()
