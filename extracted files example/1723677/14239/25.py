# PLOT INTERACTIONS WITH WHEEZY-MAGIC
plt.figure(figsize=(15,8))
plt.matshow(interactions.transpose(),fignum=1)
plt.title("Variable Interactions with wheezy-copper-turtle-magic \n \
    Yellow = combines to create positive correlation with target. Blue = negative correlation",fontsize=16)
plt.xlabel('values of wheezy-copper-turtle-magic')
plt.ylabel('columns of train')
plt.show()
