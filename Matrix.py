import random

class Matrix:

    #Initialise the function with either a 2 dimensional array (the matrix) 
    # or a list 2 long (the dimensions of the matrix)
    def __init__(self, matrixInfo, setRandom = False):

        #If input was a matrix
        if(type(matrixInfo[0]) == list):
            self.matrix = matrixInfo
            self.dimensions = [len(matrixInfo), len(matrixInfo[0])]

        #if input was the size of the array
        else:
            self.dimensions = matrixInfo

            if(setRandom):
                self.matrix = [ [random.random()] * matrixInfo[1] for _ in range(matrixInfo[0])]
            else:
                self.matrix = [ [0] * matrixInfo[1] for _ in range(matrixInfo[0])]

    #Initialise the matrix as the size given with each element at the number input
    def Initialise(self, dimensions, number = 0):
        self.dimensions = dimensions
        self.matrix = [ [number] * dimensions[0] for _ in range(dimensions[1])]

    #Returns a transposed version of the matrix
    def Transpose(self):
        newMatrix = Matrix([self.dimensions[1], self.dimensions[0]])

        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                newMatrix.matrix[j][i] = self.matrix[i][j]

        return newMatrix

    #Finds the result of the dot product of 2 matrices and returns it as a new matrix
    def Dot(self, other):

        newMatrix = Matrix([self.dimensions[0], other.dimensions[1]])

        for i in range(self.dimensions[0]):

            for j in range(other.dimensions[1]):
                currentTotal = 0

                for k in range(self.dimensions[1]):
                    currentTotal += self.matrix[i][k] * other.matrix[k][j]

                newMatrix.matrix[i][j] = currentTotal

        return newMatrix

    #Finds the result of multiplying a constant or another matrix to the current matrix and returns the result as a new matrix
    def Multiply(self, other):

        newMatrix = Matrix(self.dimensions)

        if(type(other) == int or type(other) == float):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] * other

        elif(type(other) == Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] * other.matrix[i][j]

        return newMatrix


    #Finds the result of adding a constant or another matrix to the current matrix and returns the result as a new matrix
    def Add(self, other):

        newMatrix = Matrix(self.dimensions)

        if(type(other) == int or type(other) == float):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] + other

        elif(type(other) == Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return newMatrix

    #Finds the result of subtracting a constant or another matrix to the current matrix and returns the result as a new matrix
    def Subtract(self, other):

        newMatrix = Matrix(self.dimensions)

        if(type(other) == int or type(other) == float):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] - other

        elif(type(other) == Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]

        return newMatrix

    #Finds the result of dividing a constant or another matrix to the current matrix and returns the result as a new matrix
    def Divide(self, other):

        newMatrix = Matrix(self.dimensions)

        if(type(other) == int or type(other) == float):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] / other

        elif(type(other) == Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    newMatrix.matrix[i][j] = self.matrix[i][j] / other.matrix[i][j]

        return newMatrix
    
    #Prints the matrix in a formatted form
    def Print(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=", ")
            print()

    #Finds the determinant of the matrix given
    def Determinant(self):

        #If matrix is just of size 2x2
        # find the determinant and return it
        if(self.dimensions[0] == 2):
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]

        #If matrix isn't 2x2
        else:

            #Loop through the top row of the matrix
            currentTotal = 0
            for i in range(self.dimensions[0]):

                #Get list of columns (not containing the current column)
                columns = list(range(self.dimensions[0]))
                columns.pop(i)

                #Create a new matrix 1 size smaller than the current matrix
                # not using the top row or current column
                newMatrix = Matrix([self.dimensions[0]-1, self.dimensions[1]-1])
                for j, row in enumerate(list(range(1, self.dimensions[0]))):
                    for k, column in enumerate(columns):
                        newMatrix.matrix[j][k] = self.matrix[row][column]

                #Do a calculation to find what the current cell of the matrix multiplied by determinant of the smaller matrix is
                partialCalculation = self.matrix[0][i]*newMatrix.Determinant()

                #if the column being looked at is an even number
                if(i % 2 == 0):

                    #Add the calculation to the total
                    currentTotal += partialCalculation
                else:
                    #Subtract the calculation from the total
                    currentTotal -= partialCalculation

            #Return the determinant
            return currentTotal

    #Calculate what the inverse of the current matrix is
    def Inverse(self):

        #Calculate the determinant
        determinant = self.Determinant()

        #If the determinant is 0 the inverse cannot be calculated
        if(determinant == 0):
            return None

        else:
            newMatrix = Matrix(self.dimensions)

            #Create Matrix of Minors
            for i in range(self.dimensions[0]):
                rows = list(range(self.dimensions[0]))
                rows.pop(i)

                for j in range(self.dimensions[1]):
                    columns = list(range(self.dimensions[1]))
                    columns.pop(j)

                    tempMatrix = Matrix([self.dimensions[0]-1, self.dimensions[1]-1])
                    for k, row in enumerate(rows):
                        for l, column in enumerate(columns):
                            tempMatrix.matrix[k][l] = self.matrix[row][column]
                    
                    newMatrix.matrix[i][j] = tempMatrix.Determinant()

            #Create Matrix of Cofactors
            for i in range(self.dimensions[0]):
                for j in range(self.dimensions[1]):
                    if(i*j+j % 2 != 0):
                        newMatrix.matrix[i][j] = -newMatrix.matrix[i][j]

            #Create Adjugate Matrix
            newMatrix = newMatrix.Transpose()

            #Create Inverse Matrix
            multiplier = 1/determinant
            newMatrix = newMatrix.Multiply(multiplier)

            return newMatrix

    def applyFunction(self, function):

        newMatrix = Matrix(self.dimensions)

        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                newMatrix.matrix[i][j] = function(self.matrix[i][j])
        
        return newMatrix