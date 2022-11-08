# This program is meant to provide many functions that can be used to help simplify writing LaTeX code.
# It is currently under development, so features are being added over time.
# The premise is that these functions will deal with a list of strings which can be printed out as the LaTeX code.

import numpy as np

# The package amsmath is required for this to compile correctly on LaTeX.
# No need for numPy for this function, as it takes the elements of a list and prints them out in LaTeX format.
# This only prints out 2D arrays.
# Prints out the LaTeX code for the matrix.
def latexMatrix(matrix, packages, matrixType = "b"): 
    if type(matrixType) != type("") or matrixType not in ["b", "p", "B", "v", "V"]: # list of common matrix types of latex
        raise TypeError("Matrix type not in list of possible types")
    if "amsmath" not in packages:
        raise TypeError("amsmath package is required")
    
    matrix = list(matrix) # Making sure it's a list, although it'd probably work if it were a numpy matrix too.

    latexCode = [] # Initialize the latex code list

    # Adds the starting part of the matrix command
    latexCode.append("\\begin{" + matrixType + "matrix}")

    # Note: you must convert all of the numbers into strings for the .join method to work.
    for row in matrix:
        if type(row) == type([]):
            # Add each element in the row to the list
            for element in row:
                latexCode.append(str(element)) # there can be any number of columns

                # Only add the "&" symbol between the elements, not after the last one
                if element != row[-1]:
                    # Add an "&" symbol in between the elements in a row
                    latexCode.append("&")
            
            # This conditional prevents it from adding "\\" after the last row
            if row != matrix[-1]:
                # After each row except for the last one, you need to add "\\"
                latexCode.append("\\\\")
        else:
            latexCode.append(str(element)) # there must only be one column, so no need to iterate row
    
    # Adds the ending part of the matrix command
    latexCode.append("\\end{" + matrixType + "matrix}")

    # Creates the string to hold the latex Code by joining the elements with spaces in between all of them
    latexCodeString = " ".join(latexCode)

    return latexCodeString

packageList = ["amsmath"]
testingMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(latexMatrix(testingMatrix, packageList))