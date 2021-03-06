import numpy as np

inputs = [1, 2, 3, 2.5]
weigths = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# ( weights[n] * inputs[n] ) + bias
output = np.dot(weigths, inputs) + biases
print(output)
