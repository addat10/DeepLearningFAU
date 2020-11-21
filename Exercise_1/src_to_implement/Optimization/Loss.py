import numpy as np
class CrossEntropyLoss():
    def __init__(self):
        self.input_tensor=None
        self.P1=None
    def forward(self, input_tensor,label_tensor):
        self.input_tensor=input_tensor
        self.P1=np.sum(np.multiply(self.input_tensor,label_tensor),axis=1)
        L=np.sum(-1*np.log(self.P1+np.finfo(float).eps),axis=0)
        return L
    def backward(self, label_tensor):
        Y_hat_inv=np.diagflat(np.reciprocal(self.P1))
        error_tensor_prev=-1*np.matmul(Y_hat_inv,label_tensor)
        return error_tensor_prev