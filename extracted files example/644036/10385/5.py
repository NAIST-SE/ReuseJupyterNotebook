# plotting only 50 examples of each
p = figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave,hover",
          plot_height=400, plot_width=800)
for plotcount in tqdm(range(0, 50)):
    p.line(train_T.sort_values('feat_mean')[negative_index[plotcount]].reset_index(drop=True).index,
           train_T.sort_values('feat_mean')[negative_index[plotcount]].reset_index(drop=True).values)
    p.line(train_T.sort_values('feat_mean')[positive_index[plotcount]].reset_index(drop=True).index,
           train_T.sort_values('feat_mean')[positive_index[plotcount]].reset_index(drop=True).values,
          color='orange')
show(p)
