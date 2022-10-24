# SEPARATE PUBLIC AND PRIVATE DATASETS
public = test[ test['id'].isin(public_ids) ].copy()
private = test[ ~test.index.isin(public.index) ].copy()
