for jc in json_cols: 
    print(jc)
    flat_df = pd.io.json.json_normalize(train_jsons[jc].apply(json.loads)) 
    flat_df = flat_df.apply(pd.to_numeric, errors='ignore')
    profile(flat_df)
