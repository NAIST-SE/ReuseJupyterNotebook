# Downsample to speed up plot time.
sns.pairplot(data=scc.sample(5000), hue='type', vars=['fc','sd','pso','dso','scalar_coupling_constant'])
plt.show()
