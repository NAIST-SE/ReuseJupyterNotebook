def plot_spectrogram(y, imgdir=None, imgname=None, plot=True, sr=10000, n_mels=1000, log_tf=True, vmin=-100, vmax=0):
    # Let's make and display a mel-scaled power (energy-squared) spectrogram
    #y = np.array([float(x) for x in df['acoustic_data'].values])
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=n_mels)

    # Convert to log scale (dB). We'll use the peak power (max) as reference.
    if log_tf:
        S = librosa.power_to_db(S, ref=np.max)
    
    if plot:
        # Make a new figure
        plt.figure(figsize=(15,5))
        plt.imshow(S)
        # draw a color bar
        plt.colorbar(format='%+02.0f dB')
        # Make the figure layout compact
        plt.tight_layout()
        plt.axis('off')
    if imgname is not None:
        plt.imsave('{}/{}.png'.format(imgdir, imgname), S)
        plt.clf()
        plt.close()
    return
