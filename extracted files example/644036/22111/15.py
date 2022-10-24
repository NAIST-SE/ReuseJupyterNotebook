mean_react = train['mean_reactivity'].mean()
mean_deg_Mg_pH10 = train['mean_deg_Mg_pH10'].mean()
mean_deg_Mg_50C = train['mean_deg_Mg_50C'].mean()

ss['reactivity'] = mean_react
ss['deg_Mg_pH10'] = mean_deg_Mg_pH10
ss['deg_Mg_50C'] = mean_deg_Mg_50C

ss.to_csv('submission.csv', index=False)
ss.head()
