train_play = train.groupby('PlayId').first()
train_top10_def = train_play.loc[train_play['DefensePersonnel'].isin(top_10_defenses)]

fig, ax = plt.subplots(figsize=(15, 5))
sns.violinplot(x='DefensePersonnel',
               y='Yards',
               data=train_top10_def,
               ax=ax)
plt.ylim(-10, 20)
plt.title('Yards vs Defensive Personnel')
plt.show()
