ITERATIONS = 800

clf = CatBoostClassifier(iterations=ITERATIONS,
                         learning_rate=0.1,
                         depth=15,
                         eval_metric='AUC',
                         random_seed = 529,
                         task_type="GPU",
                         verbose=50)

_ = clf.fit(train_dataset) #, eval_set=valid_dataset)
