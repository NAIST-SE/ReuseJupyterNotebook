
trace_nices = Scatter(
    x = nices['xcoord'],
    y = nices['ycoord'],
    mode = 'markers',
    marker = dict(
      size=7,
      color='lightgray',
      symbol='circle',
      line = dict(width = 0,
        color='gray'),
      opacity = 0.3
     ),
    text=nices['comment']
)

trace_notnices = Scatter(
    x = notnices['xcoord'],
    y = notnices['ycoord'],
    mode = 'markers',
    marker = dict(
      size=8,
      color=notnices['class'],
      symbol='triangle-up',
      line = dict(width = 0,
        color='Darkred'),
      opacity = 0.6
     ),
    text=notnices['comment']
)

data=[trace_nices, trace_notnices]

layout = Layout(
    title = 'We See You...',
    showlegend=False,
    xaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    ),
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    )
)
# Plot and embed in ipython notebook!
fig = Figure(data=data, layout=layout)
iplot(fig, filename='jupyter/scatter1')
