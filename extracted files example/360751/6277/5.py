uni2 = list(universe)

ctlist = []
i = 0  
while i < len(uni2):  
  item = str(uni2[i])
  ct = item.count(',') + 1
  ctlist.append(ct)  
  i += 1 
print('Number of Questions in all Sets: {}'.format(sum(ctlist)))
print('Lengths of Connected Sets')

# put it in d dataframe
qSets = pd.DataFrame(
    {'qid': uni2,
    'set_length': ctlist}
    )
qSets.sort_values('set_length', axis=0, ascending=False, inplace=True)
qSets.reset_index(inplace=True, drop=True)
qSets['set_id'] = qSets.index + 1
qSets.head()
