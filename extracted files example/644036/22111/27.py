fig, axs = plt.subplots(5, 5,
                        figsize=(12, 10),
                       sharex=True)
axs = axs.flatten()
i = 0
for row in train.sample(25, random_state=42).iterrows():
    myid = row[1]['id']
    reactivity_array = row[1][DEG_MG_50C_COLS].values
    sns.regplot(np.array(range(68)).reshape(-1, 1),
                reactivity_array,
                ax=axs[i],
                color=next(color_cycle))
    axs[i].set_title(myid)
    i += 1
fig.suptitle('"DEG_MG_50C" Array for 25 Train Examples with Regression Line',
             fontsize=18,
             y=1.02)
plt.tight_layout()
plt.show()
