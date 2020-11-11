import os.path
import json
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

# I added the following libraries
import os


# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        #TODO: implement constructor
        self.data_path=file_path
        self.label_path=label_path
        self.bs=batch_size
        self.ims=image_size
        self.rot=rotation
        self.mir=mirroring
        self.shuff=shuffle
        # Load Image Data
        i = 0
        images = []
        for j in range(0,100):
            filename = str(j) + '.npy'
            path = file_path + '\\' + filename
            image = np.load(path)
            images.append(image)
            i = i + 1
        print("Image files loaded")
        # Load Label Data
        f = open(self.label_path, 'r')
        labels = json.load(f)
        self.images=images
        self.labels=labels
        self.datasize=i
        self.run_id=0


    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        batch_im = []
        batch_lab =[]
        for i in range(self.run_id, self.run_id+self.bs):
            batch_im.append(self.images[i])
            batch_lab.append(self.labels[str(i)])
        self.run_id = self.run_id+self.bs
        return np.array(batch_im), np.array(batch_lab)

    def augment(self,img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function

        return img

    def class_name(self, label):
        # This function returns the class name for a specific input
        # DONE: TODO: implement class name function
        class_name = self.class_dict[label]
        return class_name
    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        [image,label]=self.next()
        fig = plt.figure()
        for i in range(0, self.bs):
            fig.add_subplot(4,3,i+1)
            plt.imshow(image[i], cmap='gray')
            plt.title(self.class_name(label[i]))
        plt.show()
