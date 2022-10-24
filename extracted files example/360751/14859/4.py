tt_bos = tt[tt.City == 'Boston'].drop_duplicates(['level_0','IntersectionId'])

points_bos = gv.Points(tt_bos, kdims=['Longitude', 'Latitude'],
                      vdims=['level_0']).opts(color='level_0', cmap=['dodgerblue', 
                      'darkorange'], width=500, height=450, alpha=0.5)

# points_bos_train = gv.Points(tt_bos[tt_bos.level_0=='train'], kdims=['Longitude', 'Latitude'], 
#                       vdims=['level_0']).opts(color='dodgerblue', width=500, height=450, 
#                       fill_alpha=0.1, line_width=1.5, size=3)

# points_bos_test = gv.Points(tt_bos[tt_bos.level_0=='test'], kdims=['Longitude', 'Latitude'], 
#                       vdims=['level_0']).opts(color='darkorange', width=500, height=450, 
#                       line_alpha=0.1, size=3)

tiles = gv.tile_sources.CartoLight()
display(points_bos * tiles)
