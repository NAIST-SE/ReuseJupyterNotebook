for i in train_identity_.columns:
    if i in ["isFraud", "TransactionDT", "TransactionID"]:
        continue
    try:
        train_identity_.loc[train_identity_["isFraud"] == 0].set_index("TransactionDT")[
            i
        ].plot(
            style=".",
            title=i,
            figsize=(15, 3),
            alpha=0.2,
            label="Not Fraud",
            rasterized=True,
        )
        train_identity_.loc[train_identity_["isFraud"] == 1].set_index("TransactionDT")[
            i
        ].plot(style=".", title=i, figsize=(15, 3), label="Fraud", alpha=0.5)
        test_identity_.set_index("TransactionDT")[i].plot(
            style=".",
            title=i,
            figsize=(15, 3),
            alpha=0.2,
            label="Test Data",
            rasterized=True,
        )
        plt.legend()
        plt.show()
    except TypeError:
        pass
