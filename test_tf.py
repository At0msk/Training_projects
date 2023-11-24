import tensorflow as tf
import numpy as np
tensor_2d = np.array(np.random.rand(4, 4), dtype='float32') 
tensor_2d_1 = np.array(np.random.rand(4, 4), dtype='float32') 
tensor_2d_2 = np.array(np.random.rand(4, 4), dtype='float32') 
m1 = tf.convert_to_tensor(tensor_2d) 
m2 = tf.convert_to_tensor(tensor_2d_1) 
m3 = tf.convert_to_tensor(tensor_2d_2) 
mat_product = tf.matmul(m1, m2) 
print((mat_det)) 
#print((mat_sum)) 
#print((mat_det))
