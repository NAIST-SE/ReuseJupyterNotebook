# MEvents['Made'] = False
# MEvents['Made'] = False
# MEvents.loc[MEvents['EventType'] == 'made2', 'Made'] = True
# MEvents.loc[MEvents['EventType'] == 'made3', 'Made'] = True
# MEvents.loc[MEvents['EventType'] == 'missed2', 'Made'] = False
# MEvents.loc[MEvents['EventType'] == 'missed3', 'Made'] = False
# MEvents.loc[MEvents['EventType'] == 'made2', 'Missed'] = False
# MEvents.loc[MEvents['EventType'] == 'made3', 'Missed'] = False
# MEvents.loc[MEvents['EventType'] == 'missed2', 'Missed'] = True
# MEvents.loc[MEvents['EventType'] == 'missed3', 'Missed'] = True

# # Average Pct Made per xy coord
# avg_made_xy = MEvents.loc[MEvents['EventType'].isin(['miss3','made3','miss2','made2']) & (MEvents['X_'] != 0)] \
#     .groupby(['X_','Y_'])['Made','Missed'].sum().reset_index()

# # .plot(x='X_',y='Y_', style='.')
# fig, ax = plt.subplots(figsize=(15, 8))
# cmap = sns.cubehelix_palette(as_cmap=True)
# ax = sns.scatterplot(data=avg_made_xy, x='X_', y='Y_', size='Made', cmap='plasma')
# ax = create_ncaa_full_court(ax, paint_alpha=0)
# ax.set_title('Number of Shots Made')
# plt.show()
