plt.figure(figsize=(15,15))
for i in range(5):
    for j in range(5):
        plt.subplot(5,5,5*i+j+1)
        plt.hist(test[str(5*i+j)],bins=100)
        plt.title('Variable '+str(5*i+j))
plt.show()
