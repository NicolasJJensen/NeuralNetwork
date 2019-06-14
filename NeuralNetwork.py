from Matrix import Matrix
import math

def Sigmoid(value):
    return 1/(1+math.exp(value*-1))

class NeuralNetwork:

    def __init__(self, structure):
        self.structure = structure
        self.weights = [0] * (len(structure)-1)
        self.biases = [0] * (len(structure)-1)

        for i in range(len(structure)-1):
            self.weights[i] = Matrix([structure[i+1], structure[i]], True)
            self.biases[i] = Matrix([structure[i+1], 1], True)

    def FeedForward(self, inputLayer):

        activationLayer = inputLayer

        for i in range(len(self.structure)-1):
            activationLayer = self.weights[i].Dot(activationLayer).Add(self.biases[i]).applyFunction(Sigmoid)

        return activationLayer


network = NeuralNetwork([2, 4, 2])

output = network.FeedForward(Matrix([
    [1],
    [1]
]))

output.Print()