# test = tt.loc[~tt['ForecastId'].isna()]
# preds = model.predict(test[FEATURES])
# tt.loc[~tt['ForecastId'].isna(),
#        'Confirmed_Cases_Diff_Pred'] = preds
# # tt['ConfirmedCases_Pred'] = tt['ConfirmedCases_Log_Pred'].apply(np.expm1)
