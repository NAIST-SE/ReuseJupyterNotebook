for i, d in tt.groupby('open_channels'):
    d.query('not drift')['signal'].value_counts() \
        .plot(figsize=(15, 5), style='.', label=i,
              title='Value Counts by Signal (Excluding Drift Sections)')
plt.legend()
plt.show()
