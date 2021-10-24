#  4 inputs, 3 neurons
# o
#   - x
# o
#   - x
# o
#   - x
# o

# Vector Inputs ( o )
inputs = [1, 2, 3, 2.5]

# Matix of Vectors weights or length for each connections ( - )
weigths = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

# Vector Biases for each connections
biases = [2, 3, 0.5]

# output ( x )
# output = inputs*weights+bias
layer_output = []   # Output of current layer

for neuron_weigths, neuron_bias in zip(weigths, biases):
    neuron_output = 0   # Output of given neuron
    for n_input, weigth in zip(inputs, neuron_weigths):
        neuron_output += n_input*weigth
    neuron_output += neuron_bias
    layer_output.append(neuron_output)

print('Layer output: ', layer_output)
