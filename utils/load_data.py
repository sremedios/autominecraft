import os
import numpy as np
import pandas as pd
import imageio
from tqdm import tqdm

def load_image_data(data_dir):
    filenames = os.listdir(data_dir)
    filenames.sort()

    imgs = []

    for filename in tqdm(filenames[:1000]):
        im = imageio.imread(os.path.join(data_dir, filename))
        imgs.append(im)

    return np.array(imgs)

def load_inputs_data(data_dir):
    f = os.listdir(data_dir)[0]
    csv = pd.read_csv(os.path.join(data_dir, f))
    return csv.values 
