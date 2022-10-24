for row in tqdm(range(0, 500)):
    target_of_this = train.loc[row]['target']
    if target_of_this == 0:
        train_T.sort_values('feat_mean')[row].plot(figsize=(15, 5), color=colors[0], alpha=0.2)
    elif target_of_this == 1:
        train_T.sort_values('feat_mean')[row].plot(figsize=(15, 5), color=colors[2], alpha=0.6)
