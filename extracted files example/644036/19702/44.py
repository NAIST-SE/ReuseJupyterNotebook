mysub = tt.dropna(subset=['ForecastId'])[['ForecastId','ConfirmedCases_Pred1','Fatalities_Pred1']]
mysub['ForecastId'] = mysub['ForecastId'].astype('int')
mysub = mysub.rename(columns={'ConfirmedCases_Pred1':'ConfirmedCases',
                      'Fatalities_Pred1': 'Fatalities'})
mysub.to_csv('submission.csv', index=False)
