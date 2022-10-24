# Example with different color schemes
fig, axs = plt.subplots(3, 2, figsize=(15, 13))
color_schemes = [['#93B7BE', '#048A81', '#2D3047'], # court, paint, lines
                ['#BFC0C0', '#7DC95E', '#648767'],
                ['#DDA448', '#BB342F', '#8D6A9F'],
                ['#13505B', '#ED4848', '#ED4848'],
                ['#161A32', '#D9DCD6', '#EAF2EF'],
                ['#020202', '#E54424', '#FFFFFF']]
idx = 0
for ax in axs.reshape(-1):
    create_ncaa_full_court(ax,
                           three_line='both',
                           paint_alpha=0.1,
                           inner_arc=True,
                           court_color=color_schemes[idx][0],
                           paint_fill=color_schemes[idx][1],
                           lines_color=color_schemes[idx][2],
                           lw=1.5)
    idx += 1

plt.tight_layout()
plt.show()
