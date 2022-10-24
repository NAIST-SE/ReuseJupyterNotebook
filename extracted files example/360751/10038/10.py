import networkx as nx

pairs_df = (1-pairs).reset_index()
G = nx.from_pandas_edgelist(pairs_df[:20], source='level_0', target='level_1', edge_attr=0)

graph_opts = dict(arrows=False,
                  node_size=5,
                  width=2,
                  alpha=0.8,
                  font_size=12,
                  font_color='darkblue',
                  edge_color='darkgray'
                 )

fig= plt.figure(figsize=(12,10))
nx.draw_spring(G, with_labels=True, **graph_opts)
