plt.figure(figsize=(10,10))
plt.scatter(train['33'],train['65'],c=train['target'])
plt.plot([-1.6,1.4],[3,-3],':k')
plt.xlabel('variable 33')
plt.ylabel('variable 65')
plt.title('Training data')
plt.show()
