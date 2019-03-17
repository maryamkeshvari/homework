import numpy

class TheBestPathWithTheCcarANN:
    def __init__(self, thetraffic = 1.0, Shortroute = 1.0, Bestasphalt= 1.0):
        # input signals values
        self.thetraffic = thetraffic
        self.Shortroute = Shortroute
        self.Bestasphalt = Bestasphalt

    def activationFunction(self, x):
	    if x >= 0.5:
		    return 1
	    else:
		    return 0
    def solve(self):
        # create inputs array
        inputs = numpy.array([self.thetraffic, self.Shortroute, self.Bestasphalt])

        # weights from input to hidden layer
        weightsInputToHidden1 = [0.25, 0.25, 0.8]
        weightsInputToHidden2 = [0.5, -0.4, 0.9]
        weightsInputToHidden = numpy.array([weightsInputToHidden1, weightsInputToHidden2])

        # weights from hidden to output layer
        weightsHiddenToOutput = numpy.array([0, 1])
        # we calculate what will come as input to hidden layer
        # multiplying weights to inputs and adding separately for 2 inputs
        hiddenInput = numpy.dot(weightsInputToHidden, inputs)
        print("hidden input: " + str(hiddenInput))

        # we apply activation function to every hidden input (2 elements)
        hiddenOutput = numpy.array([self.activationFunction(x) for x in hiddenInput])
        print("hidden output: " + str(hiddenOutput))

        # we calculate output signal
        output = numpy.dot(weightsHiddenToOutput, hiddenOutput)
        print("output: " + str(output))
        return self.activationFunction(output)
someNeuralNetwork = TheBestPathWithTheCcarANN()
print("result: " + str(someNeuralNetwork.solve()))