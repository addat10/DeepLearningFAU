import numpy as np
class SoftMax():
    def __init__(self):
        self.output=None
        self.bs=None
        self.osz=None
    def forward(self, input_tensor):
        shape=np.shape(input_tensor)
        self.bs=shape[0]
        self.osz=shape[1]
        max = np.max(input_tensor, axis=1)
        max = max.reshape(self.bs, 1)
        input_tensor = input_tensor - max
        exp_ip = np.exp(input_tensor)
        exp_ip_sums = np.sum(exp_ip, axis=1)
        normalize_ip = np.reciprocal(exp_ip_sums)
        self.output = np.matmul(np.diag(normalize_ip), exp_ip)
        return self.output
    def backward(self, error_tensor):
        M1=np.multiply(self.output,error_tensor)
        M_ones=np.ones((self.osz,self.osz))
        M2=np.matmul(M1,M_ones)
        error_tensor_prev=M1-np.multiply(M2,self.output)
        return error_tensor_prev