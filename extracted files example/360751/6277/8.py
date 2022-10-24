qTop = qRef.drop_duplicates('set_id', keep='first')
j = qTop.merge(lookup, how='left', on='qid')
j.sort_values('set_length', ascending=False).head(6)
