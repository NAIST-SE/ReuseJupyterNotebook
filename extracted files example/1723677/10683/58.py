from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn import tree
import graphviz

# LOAD TRAIN AND TEST
df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv',dtype='category',usecols=load, nrows=10000)
df_train['HasDetections'] = df_train['HasDetections'].astype('int8')
if 5244810 in df_train.index:
    df_train.loc[5244810,'AvSigVersion'] = '1.273.1144.0'
    df_train['AvSigVersion'].cat.remove_categories('1.2&#x17;3.1144.0',inplace=True)
#df_train = df_train.sample(1000000).reset_index(drop=True)
df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load, nrows=10000)
#df_test = df_test.sample(1000000).reset_index(drop=True)

# FACTORIZE
cols = [x for x in df_train.columns if x not in ['HasDetections','AvSigVersion2']]
for col in cols: factor_data(df_train, df_test, col)
for col in cols: reduce_memory(df_train, col)
for col in cols: reduce_memory(df_test, col)
categorize(df_train, df_test, cols)
# COMBINE TRAIN AND TEST
df_train['HasDetections'] = 0
df_test['HasDetections'] = 1
df_comb = pd.concat([df_train,df_test],axis=0)

# VALIDATION
model = DecisionTreeClassifier(max_leaf_nodes=5)
model.fit(df_comb[cols], df_comb['HasDetections'])
pred_val = model.predict_proba(df_comb[cols])[:,1]
print('Model One: Adversarial Training AUC = ',round( roc_auc_score(df_comb['HasDetections'],pred_val),4 ) )
#print('Adversarial Model has tree depth =',model.tree_.max_depth,'and node count =',model.tree_.node_count)
print('Adversarial Model has max_leaf_nodes=5')
# PLOT TREE                    
tree_graph = tree.export_graphviz(model, out_file=None, max_depth = 10,
        impurity = False, feature_names = cols, class_names = ['No', 'Yes'],
        rounded = True, filled= True )
graphviz.Source(tree_graph)
