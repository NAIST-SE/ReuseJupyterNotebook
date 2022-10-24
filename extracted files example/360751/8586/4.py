# make the map
output_notebook()
RU = x_range, y_range = ((2050000, 12720000), (5250000, 12000000))
plot_width  = int(750)
plot_height = int(plot_width//1.6)

def base_plot(tools='pan,wheel_zoom,reset',plot_width=plot_width, plot_height=plot_height, **plot_args):
    p = figure(tools=tools, plot_width=plot_width, plot_height=plot_height,
        x_range=x_range, y_range=y_range, outline_line_color=None,
        min_border=0, min_border_left=0, min_border_right=0,
        min_border_top=0, min_border_bottom=0, **plot_args)
    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.add_tools(BoxZoomTool(match_aspect=True))
    return p

background = "black"
export = partial(export_image, export_path="export", background=background)

def colorized_images(x_range, y_range, w=plot_width, h=plot_height):   
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(train, 'deal_x', 'deal_y', ds.count('deal_probability'))   # reference to data
    img = txf.shade(agg, cmap=list(reversed(cc.fire)), how='eq_hist')   
    return txf.dynspread(img, threshold=0.3, max_px=4)

p = base_plot(background_fill_color=background)
p.add_tile(STAMEN_TERRAIN_RETINA)
export(colorized_images(*RU),"Avito_Deals")
InteractiveImage(p, colorized_images)
