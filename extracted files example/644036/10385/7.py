for plotcount in tqdm(range(0, 5000)):
    scaleddf_T[negative_index[plotcount]].sort_values().reset_index(drop=True).plot(figsize=(15, 15), color=colors[0], alpha=0.2)
    scaleddf_T[positive_index[plotcount]].sort_values().reset_index(drop=True).plot(figsize=(15, 15), color=colors[2], alpha=0.2)
