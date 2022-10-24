tstacked = pd.DataFrame(train.question_text.str.split(expand=True).stack(), 
                columns=['token'])

tlist = tstacked.token.unique().tolist()
vlist = [nlp_lg(str).vector for str in tqdm(tlist)]
lookup = dict(zip(tlist, vlist))

tstacked['vec'] = tstacked.token.map(lookup)

colnames = ['t'+str(i) for i in range(300)]
tstacked[colnames] = pd.DataFrame(tstacked.vec.values.tolist(), 
                            index=tstacked.index)
tstacked.drop(['token', 'vec'], axis=1, inplace=True)

del tlist
del vlist
del lookup
tagg = tstacked.groupby(level=0).apply(np.mean)
del tstacked

X_vecs = tagg.values
y = train.target.values
del tagg
