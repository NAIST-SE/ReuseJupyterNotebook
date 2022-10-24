from xgboost import XGBRegressor
rf = XGBRegressor(n_estimators = 1600 , random_state = 0 , max_depth = 15)
rf.fit(x_train,cases)
cases_pred = rf.predict(x_test)
cases_pred = np.around(cases_pred,decimals = 0)
x_train_cas = []
for i in range(len(x_train)):
    x = list(x_train[i])
    x.append(cases[i])
    x_train_cas.append(x)
x_train_cas[0]
x_train_cas = np.array(x_train_cas)
rf = XGBRegressor(n_estimators = 1600 , random_state = 0 , max_depth = 15)
rf.fit(x_train_cas,fatalities)
x_test_cas = []
for i in range(len(x_test)):
    x = list(x_test[i])
    x.append(cases_pred[i])
    x_test_cas.append(x)
x_test_cas[0]
x_test_cas = np.array(x_test_cas)
fatalities_pred = rf.predict(x_test_cas)

fatalities_pred = np.around(fatalities_pred,decimals = 0)
submission['ConfirmedCases'] = cases_pred
submission['Fatalities'] = fatalities_pred
submission.to_csv("submission.csv" , index = False)
