fig, axes = plt.subplots(10, 2, figsize=(20, 30))
top20_diff = average_of_feat.sort_values('pos_neg_diff', ascending=True).tail(20)['feature'].values
ax_position = 0
for var in top20_diff:
    if var not in ['target','id']:
        for i, d in train_df.groupby('target'):
            d[var].plot(kind='hist', bins=100, alpha=0.5, title=var, label='target={}'.format(i), ax=axes.flat[ax_position])
        axes.flat[ax_position].legend()
        ax_position += 1
plt.show()
