# LABEL ENCODE ALL STRINGS
cats = ['patient_id','sex','anatom_site_general_challenge'] 
for c in cats:
    comb[c],mp = comb[c].factorize()
    print(mp)
print('Imputing Age NaN count =',comb.age_approx.isnull().sum())
comb.age_approx.fillna(comb.age_approx.mean(),inplace=True)
comb['age_approx'] = comb.age_approx.astype('int')
