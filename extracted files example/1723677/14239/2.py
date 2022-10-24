import matplotlib.pyplot as plt

# PLOT BOOLEANS OF USEFUL BLOCKS
plt.figure(figsize=(10,20))
plt.matshow(useful.transpose(),fignum=1)
plt.title('The useful datablocks of dataset', fontsize=24)
plt.xlabel('256 Variable columns', fontsize=16)
plt.ylabel('512 Partial datasets', fontsize=16)
plt.show()
