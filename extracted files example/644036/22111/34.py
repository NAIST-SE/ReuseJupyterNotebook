for t in TARGETS:
    train_long[t].dropna().astype('float').plot(kind='hist', bins=50, figsize=(10, 3), title=t)
    test_long[t].plot(kind='hist', bins=50, figsize=(10, 3), title=t)
    plt.show()
