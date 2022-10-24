# COMBINE TRAIN AND TEST TO ENCODE TOGETHER
cols = test.columns
comb = pd.concat([df[cols],test[cols]],ignore_index=True,axis=0).reset_index(drop=True)
