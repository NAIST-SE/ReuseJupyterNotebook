# Interative Plotly
mypal = cl.scales['9']['div']['Spectral']
colors = cl.interp( mypal, 15 )
annotations = []
init_notebook_mode(connected=True)
TOP_TEAMS = df.min().loc[df.min() < FIFTEENTH_SCORE].index.values
df_filtered = df[TOP_TEAMS].ffill()
df_filtered = df_filtered.iloc[df_filtered.index >= '10-01-2019']
team_ordered = df_filtered.min(axis=0) \
    .sort_values(ascending=True).index.tolist()

data = []
i = 0
for col in df_filtered[team_ordered].columns:
    data.append(go.Scatter(
                        x = df_filtered.index,
                        y = df_filtered[col],
                        name=col,
                        line=dict(color=colors[i], width=2),)
               )
    i += 1

annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='NFL Big Data Bowl Leaderboard',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))

layout = go.Layout(yaxis=dict(range=[TOP_SCORE-0.0001, 0.015]),
                   hovermode='x',
                   plot_bgcolor='white',
                  annotations=annotations,
                  )
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    legend=go.layout.Legend(
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2,
    )
)

fig.update_layout(legend_orientation="h")
fig.update_layout(template="plotly_white")
#fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGrey')
fig.update_xaxes(showgrid=False)

iplot(fig)
