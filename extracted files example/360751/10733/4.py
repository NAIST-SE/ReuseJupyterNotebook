centers = cities.groupby('mclust')['X', 'Y'].agg('mean').reset_index()
def plot_it(df, dotsize, dotcolor, dotalpha):
    p = df.hvplot.scatter('X', 'Y', size=dotsize, xlim=(0,5100), ylim=(0,3400), width=500,
            height=450, hover_cols=['mclust'], color=dotcolor, alpha=dotalpha)
    return p

cents = plot_it(centers, 30, 'darkblue', 0.5)
npole = plot_it(cities.loc[[0]], 100, 'red', 1)
cents*npole
