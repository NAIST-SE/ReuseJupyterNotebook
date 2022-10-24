train_dataset = Pool(data=X,
                  label=y,
                  cat_features=CAT_FEATS)
# valid_dataset = Pool(data=X_valid,
#                   label=y_valid,
#                   cat_features=CAT_FEATS)
test_dataset = Pool(data=X_test,
                    cat_features=CAT_FEATS)
