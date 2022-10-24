fams = pd.read_csv('../input/santa-workshop-tour-2019/family_data.csv', 
                    index_col=['n_people','family_id'])
fams = fams.sort_values(list(fams), ascending=False)
fam_sizes = pd.Series(fams.index.get_level_values(0))

fams_array = fams.to_numpy()
pref_matrix = np.zeros((5000, 101), dtype=np.int8)
for i in range(5000):
    for j in range(10):
        day = fams_array[i, j]
        pref_matrix[i, day] = j+1

pref_matrix_exp = np.repeat(pref_matrix, fam_sizes, axis=0)
pref_matrix_exp.shape
