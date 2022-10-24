bestpath = cities.loc[path, ['X', 'Y']]
clustline = bestpath.hvplot.line('X', 'Y', xlim=(0,5100), ylim=(0,3400), width=500, 
                            height=450, datashade=True, dynspread=True) 
clustline*npole
