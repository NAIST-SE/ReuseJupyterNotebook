import numpy as np, pandas as pd, os
import os, torch, gc
from PIL import Image
import matplotlib.pyplot as plt
from pytorch_pretrained_biggan import BigGAN, truncated_noise_sample

# LOAD PRETRAINED BIGGAN-DEEP-128
model = BigGAN.from_pretrained('biggan-deep-128')
