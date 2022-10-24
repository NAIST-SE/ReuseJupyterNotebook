# CLEAR GPU MEMORY
del model, output, class_vector, noise_vector, img; gc.collect()
torch.cuda.empty_cache()
