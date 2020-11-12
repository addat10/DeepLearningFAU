import numpy as np
import os
import json
import matplotlib.pyplot as plt

file_path="data\exercise_data"
label_path="data\Labels.json"

j=5

filename=str(j)+'.npy'
path = file_path + '\\' + filename
image = np.load(path)

image_flipped=np.flip(image,axis=1)
plt.imshow(image_flipped, cmap='gray')
plt.show()
