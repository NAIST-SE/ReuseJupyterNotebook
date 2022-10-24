# Example to make plot
fig, ax = plt.subplots(figsize=(15, 8))
create_ncaa_full_court(ax,
                       three_line='both',
                       paint_alpha=0.4,
                       inner_arc=True)
plt.show()
