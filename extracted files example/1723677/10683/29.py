import warnings
warnings.filterwarnings("ignore")
import seaborn as sns, matplotlib.pyplot as plt
from matplotlib import gridspec

# DENSITY PLOT AND BOXPLOT
col = 'ThreatCount'
lines = [1, 0]
plt.figure(figsize=(15,5))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
plt.subplot(gs[0])
for line in lines:
    subset = df_train[ (df_train['HasDetections'] == line) & (~df_train[col].isna())]
    sns.kdeplot(subset[col], bw=10,
                   shade=True, linewidth=3, 
                   label = line)
plt.legend(prop={'size': 16}, title = 'HasDetections')
plt.title('Density Plot of HasDetections versus "'+col+'"')
plt.xlabel(col)
plt.xlim((-50,500))
plt.ylabel('Density')
ax = plt.subplot(gs[1])
df_train2 = df_train[ ~df_train[col].isna() ]
plt.boxplot([df_train2[ df_train2['HasDetections']==0][col],df_train2[ df_train2['HasDetections']==1][col]])
plt.title('Boxplot of "'+col+'"')
plt.ylim((-50,500))
plt.xlabel('HasDetections')
ax.set_xticklabels([0,1])
plt.show()
