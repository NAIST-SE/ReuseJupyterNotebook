sns.pairplot(sampled_train, 
             hue='isFraud',
            vars=d_cols)
plt.show()
