samp_per_second = 31
ttf_array = np.concatenate([np.linspace(11, 0, samp_per_second * 11),
                np.linspace(11, 0, samp_per_second * 11),
                np.linspace(11, 0, samp_per_second * 11),
                np.linspace(5, 0, samp_per_second * 5),
                np.linspace(10, 0, samp_per_second * 10),
                np.linspace(15, 0, samp_per_second * 15),
                np.linspace(7, 0, samp_per_second * 7),
                np.linspace(15, 10, samp_per_second * 5)])
ss = pd.read_csv('../input/LANL-Earthquake-Prediction/sample_submission.csv')
ss_simulated = pd.DataFrame(ttf_array, columns=['time_to_failure'])
ss_simulated.plot(figsize=(15, 5))
