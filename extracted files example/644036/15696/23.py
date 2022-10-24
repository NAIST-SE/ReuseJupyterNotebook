fig, ax = plt.subplots(figsize=(15, 5))
ax.set_ylim(-10, 60)
ax.set_title('Yards vs Quarter')
sns.boxenplot(x='Quarter',
            y='Yards',
            data=train.sample(5000),
            ax=ax)
plt.show()
