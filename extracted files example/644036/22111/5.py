bpps_files = os.listdir('../input/stanford-covid-vaccine/bpps/')
example_bpps = np.load(f'../input/stanford-covid-vaccine/bpps/{bpps_files[0]}')
print('bpps file shape:', example_bpps.shape)
