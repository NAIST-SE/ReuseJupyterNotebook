# Create the DL-LB combos
train['DL_LB'] = train['DefensePersonnel'] \
    .str[:10] \
    .str.replace(' DL, ','-') \
    .str.replace(' LB','') # Clean up and convert to DL-LB combo
top_5_dl_lb_combos = train.groupby('DL_LB').count()['GameId'] \
    .sort_values() \
    .tail(10).index.tolist()
ax = train.loc[train['DL_LB'].isin(top_5_dl_lb_combos)] \
    .groupby('DL_LB').mean()['Yards'] \
    .sort_values(ascending=True) \
    .plot(kind='bar',
          title='Average Yards Top 5 Defensive DL-LB combos',
          figsize=(15, 5),
          color=color_pal[4])
# for p in ax.patches:
#     ax.annotate(str(round(p.get_height(), 2)),
#                 (p.get_x() * 1.005, p.get_height() * 1.015))

#bars = ax.bar(0.5, 5, width=0.5, align="center")
bars = [p for p in ax.patches]
value_format = "{:0.2f}"
label_bars(ax, bars, value_format, fontweight='bold')
plt.show()
