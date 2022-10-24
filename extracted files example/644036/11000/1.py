# Interative Plotly
init_notebook_mode(connected=True)
TOP_TEAMS = df.min().loc[df.min() < 1.29].index.values
df_filtered = df[TOP_TEAMS].ffill()
df_filtered = df_filtered.loc[df_filtered.index > '2019-04-21']
# Create a trace
data = []
for col in df_filtered.columns:
    data.append(go.Scatter(
                        x = df_filtered.index,
                        y = df_filtered[col],
                        name=col)
               )
    
iplot(data)
