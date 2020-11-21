import numpy as np
class ReLU():
    def __init__(self):
        self.neg_IDs=None
    def forward(self, input_tensor):
        A=np.copy(input_tensor)
        self.neg_IDs = np.where(A <= 0)
        A[self.neg_IDs] = 0
        return A
    def backward(self, error_tensor):
        B=np.copy(error_tensor)
        B[self.neg_IDs]=0
        return B