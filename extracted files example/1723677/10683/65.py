from keras import callbacks
from sklearn.metrics import roc_auc_score

class printAUC(callbacks.Callback):
    def __init__(self, X_train, y_train, inps, fes, X_val, y_val, k, ee):
        super(printAUC, self).__init__()
        self.bestAUC = 0
        self.X_train = X_train
        self.y_train = y_train
        self.inps = inps
        self.fes = fes
        self.X_val = X_val
        self.y_val = y_val
        self.k = k
        self.ee = ee
        
    def on_epoch_end(self, epoch, logs={}):
        pred = self.model.predict([self.X_train[col] for col in self.inps] + [self.X_train[self.fes]])
        aucTR = roc_auc_score(self.y_train, pred)
        pred = self.model.predict([self.X_val[col] for col in self.inps] + [self.X_val[self.fes]])
        auc = roc_auc_score(self.y_val, pred)
        print ("Train AUC: " + str(round(aucTR,5))+" - Validation AUC: " + str(round(auc,5)))
        if (self.bestAUC < auc) :
            self.bestAUC = auc
            self.model.save("bestNet"+str(self.k)+".h5", overwrite=True)
        return
