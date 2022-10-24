for i in train_transaction.columns:
    if i in ["isFraud", "TransactionDT", "TransactionID"]:
        continue
    try:
        train_transaction.loc[train_transaction["isFraud"] == 0].set_index(
            "TransactionDT"
        )[i].sample(10000).plot(
            style=".",
            title=i,
            figsize=(15, 3),
            alpha=0.05,
            label="Not Fraud",
            rasterized=True,
        )
        train_transaction.loc[train_transaction["isFraud"] == 1].set_index(
            "TransactionDT"
        )[i].sample(10000).plot(
            style=".",
            title=i,
            figsize=(15, 3),
            label="Fraud",
            alpha=0.05,
            rasterized=True,
        )

        test_transaction.set_index("TransactionDT")[i].sample(10000).plot(
            style=".",
            title=i,
            figsize=(15, 3),
            alpha=0.05,
            label="Test Data",
            rasterized=True,
        )

        plt.legend()
        plt.show()
    except TypeError:
        pass
