# CONVERT VARIABLES TO MODEL TWO
for col in cols: relax_data(df_train, df_test, col)
categorize(df_train, df_test, cols)
df_comb = pd.concat([df_train,df_test],axis=0)
# REMOVE TROUBLESOME SMODE
cols2 = cols.copy()
cols2.remove('SMode')

#VALIDATION
model = DecisionTreeClassifier(max_leaf_nodes=5)
model.fit(df_comb[cols2], df_comb['HasDetections'])
pred_val = model.predict_proba(df_comb[cols2])[:,1]
print('Model Two: Adversarial Training AUC = ',round( roc_auc_score(df_comb['HasDetections'],pred_val),4 ) )
#print('Adversarial Model has tree depth =',model.tree_.max_depth,'and node count =',model.tree_.node_count)
print('Adversarial Model has max_leaf_nodes=5')
# PLOT TREE          
tree_graph = tree.export_graphviz(model, out_file=None, max_depth = 10,
        impurity = False, feature_names = cols2, class_names = ['No', 'Yes'],
        rounded = True, filled= True )
graphviz.Source(tree_graph)
