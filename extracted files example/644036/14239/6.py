train = pd.read_csv('../input/instant-gratification/train.csv')
test = pd.read_csv('../input/instant-gratification/test.csv')
with open('../input/predictions/prediction.pkl', 'rb') as f:
    vlad_preds = pickle.load(f)
