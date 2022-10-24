# 3D Plot!
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
example = structures.loc[structures['molecule_name'] == 'dsgdb9nsd_000001']
ax.scatter(xs=example['x'], ys=example['y'], zs=example['z'], s=100)
plt.suptitle('dsgdb9nsd_000001')
plt.show()
