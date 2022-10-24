def mean_absolute_error(pred:Tensor, targ:Tensor)->Rank0Tensor:
    "Mean absolute error between `pred` and `targ`."
    pred,targ = flatten_check(pred,targ)
    return torch.abs(targ - pred).mean()

learn = cnn_learner(data, models.resnet50, metrics=mean_absolute_error)
learn.fit_one_cycle(4, 0.01)
