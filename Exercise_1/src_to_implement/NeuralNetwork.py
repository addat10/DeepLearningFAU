import numpy as np
import copy
class NeuralNetwork():
    def __init__(self,optimizer):
        self.optimizer=optimizer
        self.loss=[]
        self.layers=[]
        self.data_layer=None
        self.loss_layer=None
        self.data_input_tensor=None
        self.data_label_tensor=None
    def forward(self):
        [self.data_input_tensor,self.data_label_tensor]=self.data_layer.next()
        tensor=np.copy(self.data_input_tensor)
        for layer_curr in self.layers:
            tensor=layer_curr.forward(tensor)
        output_tensor=self.loss_layer.forward(tensor,self.data_label_tensor)
        return output_tensor
    def backward(self):
        error_tensor=self.loss_layer.backward(self.data_label_tensor)
        for layer_curr in reversed(self.layers):
            error_tensor=layer_curr.backward(error_tensor)
    def append_trainable_layer(self,layer):
        layer.optimizer=copy.deepcopy(self.optimizer)
        self.layers.append(layer)
    def train(self,iterations):
        for i in range(iterations):
            self.loss.append(self.forward())
            self.backward()
    def test(self,input_tensor):
        tensor=np.copy(input_tensor)
        for layer_curr in self.layers:
            tensor=layer_curr.forward(tensor)
        return tensor