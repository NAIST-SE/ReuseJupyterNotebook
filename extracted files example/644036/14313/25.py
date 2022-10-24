atom_count_dict = structures.groupby('molecule_name').count()['atom_index'].to_dict()
