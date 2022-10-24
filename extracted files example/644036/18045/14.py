for i, d in tt.groupby('open_channels'):
    d.query('drift')['signal_round4'] \
        .round(4).value_counts() \
        .plot(figsize=(15, 5), style='.', label=i,
             title='Unique Value Counts in Drift Data after Shifting to Optimize Anchors')
plt.legend()
plt.show()
