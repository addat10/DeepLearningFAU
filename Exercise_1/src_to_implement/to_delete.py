import numpy as np

'''
input_tensor=np.array([[1,2],[3,4]])
shape=np.shape(input_tensor)
max = np.max(input_tensor, axis=1)
max = max.reshape(shape[0], 1)
input_tensor = input_tensor - max
print(input_tensor)
exp_ip = np.exp(input_tensor)
print(exp_ip)
exp_ip_sums = np.sum(exp_ip, axis=1)
print(exp_ip_sums)
normalize_ip = np.reciprocal(exp_ip_sums)
print(normalize_ip)
print(np.diag(normalize_ip))
output = np.matmul(np.diag(normalize_ip), exp_ip)
print(output)
'''
'''
error_tensor=np.array([[1,2],[3,4],[5,6]])
output=np.array([[7,8],[9,10],[11,12]])
osz=2
M1 = np.multiply(output, error_tensor)
M2 = np.ones((osz,osz))
error_tensor_prev = M1 - np.matmul(M1, M2)
print(error_tensor_prev)
'''

'''
error_tensor=np.array([[1,2],[3,4],[5,6]])
output=np.array([[7,8],[9,10],[11,12]])
osz=2
M1=np.multiply(output,error_tensor)
M_ones=np.ones((osz,osz))
M2=np.matmul(M1,M_ones)
error_tensor_prev=M1-np.multiply(M2,output)
print(error_tensor_prev)
'''
'''
label_tensor=np.array([[4.0,5.0,6.0],[7.0,8.0,9.0],[10.0,11.0,12.0]])
P1=np.array([[1.0],[2.0],[3.0]])
P1=np.reshape(P1,(3,1))
Y_hat_inv=np.diagflat(np.reciprocal(P1))
error_tensor_prev=-1*np.matmul(Y_hat_inv,label_tensor)
print(Y_hat_inv)
error_tensor_prev=-1*np.matmul(Y_hat_inv,label_tensor)
print(error_tensor_prev)
'''

for i in range(3):
    print(i)
