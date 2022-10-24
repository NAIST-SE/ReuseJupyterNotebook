CONFIDENCE = 0.90

idx1 =  (train.SmokingStatus == 'Never smoked')
idx2 = (train.SmokingStatus.isin(['Ex-smoker', 'Currently smokes']))

durations1 = train.loc[idx1, 'Weeks']
durations2 = train.loc[idx2, 'Weeks']

events1 = train.loc[idx1, 'LowFVC']
events2 = train.loc[idx2, 'LowFVC']

kmf1 = KaplanMeierFitter()
kmf1.fit(durations1, events1, alpha=(1-CONFIDENCE), label='Never Smoked')

kmf2 = KaplanMeierFitter()
kmf2.fit(durations2, events2, alpha=(1-CONFIDENCE), label='Smoked')

plt.clf()
