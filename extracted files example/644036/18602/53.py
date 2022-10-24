# Example adding data 
fig, ax = plt.subplots(figsize=(15, 8))
create_ncaa_full_court(ax,
                       three_line='both',
                       paint_alpha=0.4,
                       inner_arc=True)
for i, d in MEvents.query('PlayerID == 13061 and X_ != 0').groupby('EventType'):
    d.plot(x='X_', y='Y_', style='X', ax=ax, label=i, alpha=1)
    plt.legend()
plt.show()
