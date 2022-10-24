fig, ax = plt.subplots(figsize=(15, 5))
ax.set_ylim(-10, 60)
sns.boxenplot(x='DefendersInTheBox',
               y='Yards',
               data=train.query('DefendersInTheBox > 2'),
               ax=ax)
plt.title('Yards vs Defenders in the Box')
plt.show()
