import numpy as np
class FullyConnected(object):
    def __init__(self,input_size,output_size):
        self.isz=input_size
        self.osz=output_size
        self.weights=np.random.rand(self.isz+1,self.osz)
        self.input_wb=None
        self._gradient_weights=None
        self._optimizer=None
        self.opt_flag = 0
    def forward(self,input_tensor):
        bs=np.size(input_tensor,0)
        bias=np.ones((bs,1))
        self.input_wb=np.concatenate([input_tensor,bias],axis=1)
        output=np.matmul(self.input_wb,self.weights)
        return output
    def backward(self,error_tensor):
        E_prev=np.matmul(error_tensor,np.transpose(self.weights[0:(self.isz),:]))
        self._gradient_weights=np.matmul(np.transpose(self.input_wb),error_tensor)
        if (self.opt_flag!=0):
            self.weights=self._optimizer.calculate_update(self.weights,self._gradient_weights)
        return E_prev
    @property
    def optimizer(self):
        return self._optimizer
        print('getting optimizers')
    @optimizer.setter
    def optimizer(self, opt):
        self.opt_flag = 1
        self._optimizer = opt
        print('setting opt')
    @property
    def gradient_weights(self):
        return self._gradient_weights
    @gradient_weights.setter
    def gradient_weights(self,dW):
        self._gradient_weights=dW