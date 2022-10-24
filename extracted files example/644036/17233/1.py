plt.style.use('bmh')
plt.rcParams["font.size"] = "12"
ALL_TEAMS = df.columns.values
df_ffill = df[ALL_TEAMS[1:]].ffill()

# This is broken
df_ffill.plot(figsize=(20, 10),
              color=color_pal[0],
              legend=False,
              alpha=0.05,
              ylim=(68850-1000, 80850),
              title='All Teams Public LB Scores over Time')

df.ffill().min(axis=1).plot(color=color_pal[1], label='1st Place Public LB', legend=True)
plt.show()
