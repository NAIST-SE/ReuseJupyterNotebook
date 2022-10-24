train_expanded = pd.concat([train, train['PredictionString'].str.split(' ', expand=True)], axis=1)
train_expanded = train_expanded.rename(columns={0 : '1_model_type', 1 : '1_yaw', 2 : '1_pitch',
                                                3 : '1_roll', 4 : '1_x', 5 : '1_y', 6 : '1_z'})
train_expanded.drop('PredictionString', axis=1).head()
