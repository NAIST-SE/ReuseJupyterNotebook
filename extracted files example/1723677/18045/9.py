sub = pd.read_csv('../input/liverpool-ion-switching/sample_submission.csv')
sub.open_channels = test_pred
sub.to_csv('submission.csv',index=False,float_format='%.4f')

res=200
plt.figure(figsize=(20,5))
plt.plot(sub.time[::res],sub.open_channels[::res])
plt.show()
