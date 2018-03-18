from models.crnn import crnn
from utils.load_data import load_image_data, load_inputs_data
import numpy as np
import os
import imageio

DATA_DIR = os.path.join("data", "train")
IMG_DIR = os.path.join(DATA_DIR, "images")
INPUTS_DIR = os.path.join(DATA_DIR, "inputs")

########## LOAD DATA ##########

X = load_image_data(IMG_DIR) 
Y = load_inputs_data(INPUTS_DIR)

Y = Y[:1000,:]
print(X.shape)
print(Y.shape)

model = crnn(X[0].shape, Y[0].shape)
model.fit(X,Y,epochs=100,batch_size=16,validation_split=0.2)
