from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
init_notebook_mode(connected=False)

# create datafRAME WITH comments, target, tsnex,tsney
#separate into 2 groups of x_nice, x_notnice, y_nice, y_notnice
plotme = pd.DataFrame({'comment':train_text, 'class':train_tgt, 'xcoord': x_tsne, 'ycoord':y_tsne})
nices = plotme[plotme['class'] == 0]
notnices = plotme[plotme['class'] > 0]

