from generator import ImageGenerator
# Settings
file_path="data\exercise_data"
label_path="data\Labels.json"
batch_size=10
image_size=10
rotation=False
mirroring=False
shuffle=False
# Create an object of the class
Image_set_1=ImageGenerator(file_path, label_path, batch_size, image_size, rotation, mirroring, shuffle)
Image_set_1.show()
Image_set_1.show()

Image_set_1.show()
Image_set_1.show()
