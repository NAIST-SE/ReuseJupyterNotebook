PATH = '../input/melanoma-oof-and-sub/'
FILES = os.listdir(PATH)

OOF = np.sort( [f for f in FILES if 'oof' in f] )
OOF_CSV = [pd.read_csv(PATH+k) for k in OOF]

print('We have %i oof files...'%len(OOF))
print(); print(OOF)
