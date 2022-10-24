tt_phi = tt[tt.City == 'Philadelphia'].drop_duplicates(['level_0','IntersectionId'])
points_phi = gv.Points(tt_phi, kdims=['Longitude', 'Latitude'],
                      vdims=['level_0']).opts(color='level_0', cmap=['dodgerblue', 
                      'darkorange'], width=500, height=450, alpha=0.5)
tiles = gv.tile_sources.CartoLight()
display(tiles*points_phi)
