from neuralNetwork import neuralNetwork
import numpy
import matplotlib.pyplot

# number of input, hidden and output
# input_nodes= 3
# hidden_nodes = 3
# output_nodes = 3
# # learning rate is 0.3
# learning_rate = 0.3
# #create instance of nueral network
# n = neuralNetwork(input_nodes,hidden_nodes, output_nodes, learning_rate)
# #query it with random inputs and output result
# output = n.query([1.0,0.5,-1.5])
# print(output)

# Reading test file
data_file = open("data/mnist_train_100.csv", 'r')
data_list = data_file.readlines()
data_file.close()

all_values = data_list[1].split(',')
scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
print(scaled_input)
matplotlib.pyplot.savefig("output/samplePlot2.png")

