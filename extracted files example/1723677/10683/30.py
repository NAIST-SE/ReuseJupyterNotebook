del df_train['DateAS'], df_train['DateOS'], df_train['DateBL'], df_train['WeekOf'] 
del df_train['AvSigVersion'], df_train['OsBuildLab'], df_train['Census_OSVersion']
print('TRAIN DATA')
df_train.sample(5)
