# Idea from https://www.kaggle.com/kevinbonnes/transactiondt-starting-at-2017-12-01
# Read his kernel it's great!
def convert_TranactionDT(df):
    try:
        START_DATE = "2017-12-01"
        startdate = datetime.datetime.strptime(START_DATE, "%Y-%m-%d")
        df["TransactionDT"] = df["TransactionDT"].apply(
            lambda x: (startdate + datetime.timedelta(seconds=x))
        )
        return df
    except TypeError:
        """Already converted?"""
        return df

train_transaction = convert_TranactionDT(train_transaction)
test_transaction = convert_TranactionDT(test_transaction)
train_identity_ = convert_TranactionDT(train_identity_)
test_identity_ = convert_TranactionDT(test_identity_)
