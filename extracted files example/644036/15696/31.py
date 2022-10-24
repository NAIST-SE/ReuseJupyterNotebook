play_id = train.query("DL_LB == '4-2'")['PlayId'].reset_index(drop=True)[500]
fig, ax = create_football_field()
train.query("PlayId == @play_id and Team == 'away'") \
    .plot(x='X', y='Y', kind='scatter', ax=ax, color='orange', s=200, legend='Away')
train.query("PlayId == @play_id and Team == 'home'") \
    .plot(x='X', y='Y', kind='scatter', ax=ax, color='blue', s=200, legend='Home')
train.query("PlayId == @play_id and NflIdRusher == NflId") \
    .plot(x='X', y='Y', kind='scatter', ax=ax, color='red', s=200, legend='Rusher')
rusher_row = train.query("PlayId == @play_id and NflIdRusher == NflId")
yards_covered = rusher_row["Yards"].values[0]

x = rusher_row["X"].values[0]
y = rusher_row["Y"].values[0]
rusher_dir = rusher_row["Dir"].values[0]
rusher_speed = rusher_row["S"].values[0]
dx, dy = get_dx_dy(rusher_dir, rusher_speed)
yards_gained = train.query("PlayId == @play_id")['Yards'].tolist()[0]
ax.arrow(x, y, dx, dy, length_includes_head=True, width=0.3)
plt.title(f'Example of a 4-2 Defense - run resulted in {yards_gained} yards gained', fontsize=20)
plt.legend()
plt.show()
