from generator import ImageGenerator
# Settings
file_path="data\exercise_data"
label_path="data\Labels.json"
batch_size=12
image_size=10
rotation=False
mirroring=False
shuffle=True
# Create an object of the class
Image_set_1=ImageGenerator(file_path, label_path, batch_size, image_size, rotation, mirroring, shuffle)
for j in range(1,10):
    Image_set_1.show()

