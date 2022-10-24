fig, ax = plt.subplots(figsize=(20, 5))
sns.violinplot(x='Distance-to-Gain',
               y='Yards',
               data=train.rename(columns={'Distance':'Distance-to-Gain'}),
               ax=ax)
plt.ylim(-10, 20)
plt.title('Yards vs Distance-to-Gain')
plt.show()
