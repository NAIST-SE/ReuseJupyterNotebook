# Interative Plotly
init_notebook_mode(connected=True)
TOP_TEAMS = df.min().loc[df.max() > FIFTEENTH_SCORE].index.values
df_filtered = df[TOP_TEAMS].ffill()
df_filtered = df_filtered.iloc[df_filtered.index > '06-3-2019']
# Create a trace
data = []
for col in df_filtered.columns:
    data.append(go.Scatter(
                        x = df_filtered.index,
                        y = df_filtered[col],
                        name=col)
               )
layout = go.Layout(yaxis=dict(range=[0.9746, TOP_SCORE+0.0001]))
fig = go.Figure(data=data, layout=layout)
iplot(fig)
