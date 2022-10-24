metadata['label_binary'] = 0
metadata.loc[metadata['label'] == "FAKE", 'label_binary'] = 1
