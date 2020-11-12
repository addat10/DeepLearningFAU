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
        # Load Label Data
        f = open(self.label_path, 'r')
        labels = json.load(f)
        # Load Image Data
        images = []
        labels1=[]
        indices=np.arange(0,100)
        if self.shuff: np.random.shuffle(indices)
        for j in indices:
            filename = str(j) + '.npy'
            path = file_path + '\\' + filename
            image = np.load(path)
            images.append(image)
            labels1.append(labels[str(j)])
        print("Image files loaded")

        self.images=images
        self.labels=labels1
        self.datasize=100
        self.run_id=0


    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        batch_im = []
        batch_lab =[]
        self.run_id = np.remainder(self.run_id, 99)

        for i in range(self.run_id, self.run_id+self.bs):
            k = np.remainder(i, 100)
            next_im=self.images[k]
            next_im=self.augment(next_im)
            batch_im.append(next_im)
            batch_lab.append(self.labels[k])
        self.run_id = self.run_id+self.bs

        return np.array(batch_im), np.array(batch_lab)

    def augment(self,img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function
        if self.mir:
            if np.random.rand() < 0.5:
                mirr_axis = 0
                if np.random.rand() < 0.5: mirr_axis = 1
                img = np.flip(img, axis=mirr_axis)
        if self.rot:
            if np.random.rand() < 0.5:
                rot_times = 1
                if np.random.rand() > 0.33 and np.random.rand() < 0.66:
                    rot_times = 2
                if np.random.rand() > 0.66:
                    rot_times = 3
                img = np.rot90(img, rot_times)

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
