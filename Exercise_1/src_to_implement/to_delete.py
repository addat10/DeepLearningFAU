import numpy as np

input_tensor = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]], dtype=float)
print(input_tensor)
print(input_tensor.shape)
bs = np.size(input_tensor, axis=0)
bias=np.ones((bs, 1))
print(bias)
print(bias.shape)

input_wb = np.concatenate([input_tensor, bias], axis=1)
print(input_wb)
#output = np.matmul(input_wb, self.weights)
