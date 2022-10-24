train['SnapHandoffSeconds'] = (pd.to_datetime(train['TimeHandoff']) - \
                               pd.to_datetime(train['TimeSnap'])).dt.total_seconds()

(train.groupby('SnapHandoffSeconds').count() / 22 )['GameId'].plot(kind='bar',
                                                                   figsize=(15, 5))
bars = [p for p in ax.patches]
value_format = "{}"
label_bars(ax, bars, value_format, fontweight='bold')
plt.show()
