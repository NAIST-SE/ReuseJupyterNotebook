sns.set()
plt.figure(figsize=(15,10))
heat_opts = {'cmap': ['#ffffff']+(cc.kbc),
             'xticklabels': 10,
             'yticklabels': False,
             'cbar_kws': {'label': 'Choice (top choice is dark)',
                          'shrink': 0.5
                          }
             }
ax=sns.heatmap(pref_matrix_exp, **heat_opts)
ax.invert_xaxis()
plt.xlabel('Days before Christmas', fontsize=14)
plt.ylabel('Families (larger families have taller blocks)',
           fontsize=14)
plt.title('Christmas Eve remains popular across a wide spectrum of preferred dates.', 
            fontsize=16, color='midnightblue')
plt.show()
