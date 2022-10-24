# Configurables
FEATURES = ['atom_index_0', 'atom_index_1',
            'atom_0_cat',
            'x_0', 'y_0', 'z_0',
            'atom_1_cat', 
            'x_1', 'y_1', 'z_1', 'dist', 'dist_to_type_mean',
            'atom_count',
            '1JHC', '1JHN', '2JHC', '2JHH', '2JHN', '3JHC', '3JHH', '3JHN'
           ]
TARGET = 'scalar_coupling_constant'
CAT_FEATS = ['atom_0','atom_1']
N_ESTIMATORS = 2000
VERBOSE = 500
EARLY_STOPPING_ROUNDS = 200
RANDOM_STATE = 529

X = train_df[FEATURES]
X_test = test_df[FEATURES]
y = train_df[TARGET]
