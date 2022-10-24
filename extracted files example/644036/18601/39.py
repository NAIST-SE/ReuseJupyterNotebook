# # Average Points Scored per xy coord
# avg_pnt_xy = MEvents.loc[MEvents['EventType'].isin(['miss3','made3','miss2','made2']) & (MEvents['X_'] != 0)] \
#     .groupby(['X_','Y_'])['PointsScored'].mean().reset_index()

# # .plot(x='X_',y='Y_', style='.')
# fig, ax = plt.subplots(figsize=(15, 8))
# ax = sns.scatterplot(data=avg_pnt_xy, x='X_', y='Y_', hue='PointsScored', cmap='coolwarm')
# ax = create_ncaa_full_court(ax)
# plt.show()
