test['ConfirmedCases_Log_Pred'] = reg.predict(test[FEATURES])
test['ConfirmedCases_pred'] = test['ConfirmedCases_Log_Pred'].apply(np.expm1)
