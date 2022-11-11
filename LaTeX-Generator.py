# This program is meant to provide many functions that can be used to help simplify writing LaTeX code.
# It is currently under development, so features are being added over time.
# The premise is that these functions will deal with a list of strings which can be printed out as the LaTeX code.

import numpy as np
import math

def iterateMatrix(matrix, function = lambda x: x):
    matrix = np.array(matrix) # Making sure it's a numpy array
    for idx, val in np.ndenumerate(matrix):
        matrix[idx] = function(val) # Replaces the value in the matrix with the value after it is input to the function provided.
                                    # NOTE: numpy arrays are mutable, so this will actually change the original array.
    return matrix

def roundMatrix(matrix, numDigits):
    return iterateMatrix(matrix, lambda x: round(x, numDigits)) # Iterates through the matrix, rounding each element, then returning it.

def convertIntsInMatrix(matrix):
    return iterateMatrix(matrix, lambda x: int(x) if x == math.floor(x) else x) # If the entry is the same value as its floor, it is an integer, so it converts it.

def isListOrArray(input):
    if type(input) in [type([]), type(np.arr([]))]:
        return True
    else:
        return False

# The package amsmath is required for this to compile correctly on LaTeX.
# No need for numPy for this function, as it takes the elements of a list and prints them out in LaTeX format.
# This only prints out 2D arrays.
# Prints out the LaTeX code for the matrix.
def latexMatrix(matrix, packages, matrixType = "b"): 
    """
    Takes a matrix and converts it into a string that contains the LaTeX code for displaying the matrix provided. 
    matrixType must be "b", "p", "B", "v", or "V". Packages are required to make sure amsmath is being used.
    """
    if type(matrixType) != type("") or matrixType not in ["b", "p", "B", "v", "V"]: # list of common matrix types of latex
        raise TypeError("Matrix type not in list of possible types")
    if "amsmath" not in packages:
        raise TypeError("amsmath package is required")
    
    # matrix = list(matrix) # Making sure it's a list, although it'd probably work if it were a numpy matrix too.
    matrix = np.array(matrix) # Trying it out if I make it an array


    latexCode = [] # Initialize the latex code list

    # Adds the starting part of the matrix command
    latexCode.append("\\begin{" + matrixType + "matrix}")

    # Note: you must convert all of the numbers into strings for the .join method to work.
    for row in matrix:
        if matrix.ndim == 2: # type(row) == type([]):
            # Add each element in the row to the list
            for elementIdx in range(len(row)):
                element = row[elementIdx] # if I don't do it this way, it won't work with numpy arrays
                latexCode.append(str(element)) # there can be any number of columns

                # Only add the "&" symbol between the elements, not after the last one
                if element != row[-1]:
                    # Add an "&" symbol in between the elements in a row
                    latexCode.append("&")
            
            print(matrix[-1])
            print(row)
            print(row.all == matrix[-1].all)

            # This conditional prevents it from adding "\\" after the last row
            if row.all != matrix[-1].all:
                # After each row except for the last one, you need to add "\\"
                latexCode.append("\\\\")
        else:
            latexCode.append(str(row)) # there must only be one column, so no need to iterate row
    
    # Adds the ending part of the matrix command
    latexCode.append("\\end{" + matrixType + "matrix}")

    # Creates the string to hold the latex Code by joining the elements with spaces in between all of them
    latexCodeString = " ".join(latexCode)

    return latexCodeString

# This is a shorthand for the inverse method in numPy
def inverse(matrix):
    matrix = np.array(matrix) # Making sure it's a numPy array

    return np.linalg.inv(matrix) # Returns in the inverse of the matrix as a numpy array

# This is just a shorthand for the determinant method in numPy
def det(matrix):
    matrix = np.array(matrix) # Making sure it's a numPy array

    return np.linalg.det(matrix) # Returns the determinant of the matrix

def transpose(matrix):
    matrix = np.array(matrix) # Making sure it's a numPy array

    return matrix.T # Returns the transpose of the matrix

def cofactor(matrix):
    matrix = np.array(matrix)
    determinant = det(matrix)
    inv = inverse(matrix)
    
    if determinant != 0:
        return roundMatrix(transpose(inv) * determinant, 10) # Need to round because sometimes the floating point operations can result in weird decimals
    else:
        raise ValueError("Determinant was zero - matrix was singular")




# MAIN #

packageList = ["amsmath"]
testingMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(type(np.array(testingMatrix)[0][0]))

print(iterateMatrix(np.array(testingMatrix), lambda x: 2 * x))

v = roundMatrix([1.000000000000005, 3.0045, 10.05], 10)

print(v[0])

print(convertIntsInMatrix(v))

print(convertIntsInMatrix(cofactor(testingMatrix)))
# print(latexMatrix(testingMatrix, packageList))

# print(latexMatrix(cofactor(testingMatrix), packageList))