coords = cities.loc[opoints.stoppt, ['X', 'Y', 'mclust']]
stops = plot_it(coords, 30, 'darkblue', 0.5)
stopsline = coords.hvplot.line('X', 'Y', xlim=(0,5100), ylim=(0,3400), color='green', width=500, 
                            height=450, hover=False) 
stopsline*npole*gausses*stops
