import seaborn as sns
import matplotlib.pyplot as plt

idx = df.loc[ df['A']!=0, 'var' ].values
idx = np.sort(idx); idx2 = []
for i in idx: idx2.append(str(i))

plt.figure(figsize=(15,15))
sns.heatmap(train[idx2+['target']].corr(), cmap='RdBu_r', annot=True, center=0.0)
plt.title('Correlation Among Useful Variables',fontsize=20)
plt.show()
