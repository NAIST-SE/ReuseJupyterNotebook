# Half Court Example
fig, ax = plt.subplots(figsize=(13.8, 14))
MEvents \
    .query('Y_ != 0') \
    .plot(x='Y_half_', y='X_half_', style='.',
          kind='scatter', ax=ax,
          color='orange', alpha=0.05)
create_ncaa_half_court(ax, court_color='black',
                       lines_color='white', paint_alpha=0,
                       inner_arc=True)
plt.show()
