sns.set()
plt.figure(figsize=(15,10))
heat_opts = {'cmap': cc.bmy,
             'xticklabels': 10,
             'yticklabels': False,
             'cbar_kws': {'label': 'Cost (USD)',
                          'shrink': 0.5
                          }
             }
ax=sns.heatmap(cost_matrix[fams_sorted], **heat_opts)
ax.invert_xaxis()
plt.xlabel('Days before Christmas', fontsize=14)
plt.ylabel('Families (larger families at top)', fontsize=14)
plt.title('Santa pays out if big families don\'t get their preference.', 
            fontsize=16, color='midnightblue')
plt.show()
