# Plot the distribution of potential_energy
pote['potential_energy'].plot(kind='hist',
                              figsize=(15, 5),
                              bins=500,
                              title='Distribution of Potential Energy',
                              color='b')
plt.show()
