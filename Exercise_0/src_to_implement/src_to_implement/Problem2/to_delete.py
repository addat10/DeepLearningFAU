import numpy as np
import os
import json
import matplotlib.pyplot as plt

file_path="data\exercise_data"
label_path="data\Labels.json"

images = []
i=0
for filename in os.listdir(file_path):
    path = file_path + '\\' + filename
    image = np.load(path)
    images.append(image)
    i = i + 1


f = open(label_path, 'r')
labels = json.load(f)

j=55
class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
plt.imshow(images[j], cmap='gray')
plt.title(class_dict[labels[str(j)]])
plt.show()
