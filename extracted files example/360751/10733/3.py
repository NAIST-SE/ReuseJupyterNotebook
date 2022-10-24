histo = cities.hvplot.hist('mclust', ylim=(0,14000), color='tan')

custcolor = cc.rainbow + cc.rainbow
gausses = cities.hvplot.scatter('X', 'Y',  by='mclust', size=5, width=500, height=450, 
                datashade=True, dynspread=True, cmap=custcolor)
display(histo, gausses)
