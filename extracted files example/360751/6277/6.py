# separate out the integers from the lists
qSetsS = qSets.loc[qSets['set_length'] == 1] 
qSetsL = qSets.loc[qSets['set_length'] > 1] 

# unnest
rows = []
_ = qSetsL.apply(lambda row: [rows.append([row['set_id'], row['set_length'], nn]) 
                         for nn in row.qid], axis=1)

qRef = pd.DataFrame(rows, columns = ['set_id', 'set_length', 'qid'])

qRef = qRef.append(qSetsS)
qRef.sort_values('qid', inplace=True)
qRef.reset_index(inplace=True, drop=True)
qRef.to_csv('qRef.csv', index=False)
qRef.head()
