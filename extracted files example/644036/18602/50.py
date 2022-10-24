# Made and Missed shots dataframes
WMadeShots = WEvents.query('EventType == "made2" or EventType == "made3"')
WMissedShots = WEvents.query('EventType == "miss2" or EventType == "miss3"')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
ax1 = create_ncaa_half_court(ax=ax1,
                             three_line='womens',
                             court_color='white',
                             paint_alpha=0,
                             inner_arc=True)
ax2 = create_ncaa_half_court(ax=ax2,
                             three_line='womens',
                             court_color='white',
                             paint_alpha=0,
                             inner_arc=True)
hb1 = ax1.hexbin(x=WMadeShots.query('Y_ != 0')['Y_half_'],
                 y=WMadeShots.query('Y_ != 0')['X_half_'],
                 gridsize=20, bins='log', cmap='inferno')
hb2 = ax2.hexbin(x=WMissedShots.query('Y_ != 0')['Y_half_'],
                 y=WMissedShots.query('Y_ != 0')['X_half_'],
                 gridsize=20, bins='log', cmap='inferno')
ax1.set_title('Womens NCAA Made Shots', size=15)
ax2.set_title('Womens NCAA Missed Shots', size=15)
cb1 = fig.colorbar(hb1, ax=ax1)
cb1 = fig.colorbar(hb2, ax=ax2)
plt.tight_layout()
plt.show()
