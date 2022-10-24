import hvplot.pandas
opts = {'invert_yaxis': False,
        'yticks': list(range(0,100,20)),
        'padding': 0.1,
        'width':450,
        'height': 300,
           }

# df = bos
# aggfunc='mean'
def make_plot(df, aggfunc):
    assert (aggfunc == 'mean') | (aggfunc == 'std')
    paths = df.set_index(('', 'Path')).loc[:, aggfunc].reset_index()
    paths.columns = [paths.columns[0][1]] + [c[-4:] for c in paths.columns[1:]]
    plot = hvplot.parallel_coordinates(paths, 'Path', **opts)
    if aggfunc == 'mean':
        return plot.options(ylabel='Mean Wait Time')
    else:
        return plot.options(ylabel='STD of Wait Times', show_legend=False)

land_cambridge = make_plot(bos, 'mean').options(title="Land & Cambridgeside") +\
    make_plot(bos, 'std')
fifth_cambria = make_plot(phi, 'mean').options(title="5th & Cambria") +\
    make_plot(phi, 'std')

display(land_cambridge, fifth_cambria)
