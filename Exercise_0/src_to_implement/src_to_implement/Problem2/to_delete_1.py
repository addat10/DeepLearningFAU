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

plt.imshow(image, cmap='gray')
plt.show()
