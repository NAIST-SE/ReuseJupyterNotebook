plt.figure(figsize=(15,5))
plt.plot(h.history['acc'],label='Train ACC')
plt.plot(h.history['val_acc'],label='Val ACC')
plt.title('TRAIN COMPARED WITH TEST. Training History')
plt.legend()
plt.show()
