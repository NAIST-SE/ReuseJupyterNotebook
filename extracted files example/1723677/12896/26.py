# GENERATE USELESS VARIABLES AND RANDOM TARGETS
public = pd.DataFrame(np.zeros((1975,300)))
for i in range(300): public.iloc[:,i] = np.random.normal(0,1,1975)
public['target'] = np.random.uniform(0,1,1975)
public.loc[ public['target']>0.34, 'target'] = 1.0
public.loc[ public['target']<=0.34, 'target'] = 0.0
