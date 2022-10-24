for surface in y_train['surface'].unique():
    first = y_train.loc[y_train['surface'] == surface].index[0]
    series = X_train.loc[X_train['series_id'] == first]
    p = figure(width=1000, height=200, title='{}- linear acceleration'.format(surface))
    source = ColumnDataSource(series)
    avX = p.line(x='measurement_number', y='linear_acceleration_X', source=source, color='red')
    p.add_tools(HoverTool(tooltips='linear_acceleration_X', renderers=[avX]))
    avY = p.line(x='measurement_number', y='linear_acceleration_Y', source=source, color='blue')
    p.add_tools(HoverTool(tooltips='linear_acceleration_Y', renderers=[avY]))
    avZ = p.line(x='measurement_number', y='linear_acceleration_Z', source=source, color='orange')
    p.add_tools(HoverTool(tooltips='linear_acceleration_Z', renderers=[avZ]))
    show(p)
