#!/usr/bin/python3
"""this module divides int or float numbers stored in matrix"""

def matrix_divided(matrix, div):
   """Divides all elements of a matrix by a number, with error handling and rounding.

   Args:
       matrix: A list of lists of integers or floats representing a matrix.
       div: A number (integer or float) to divide the elements by.

   Returns:
       A new matrix with the same dimensions as the input matrix, where each
       element has been divided by div and rounded to 2 decimal places.

   Raises:
       TypeError: If matrix is not a list of lists of integers or floats,
           if the rows of the matrix have different lengths, or if div is not a number.
       ZeroDivisionError: If div is equal to 0.
   """

   if type(matrix) is not list or not all(type(row) is list for row in matrix):
       raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
   if not all(len(row) == len(matrix[0]) for row in matrix):
       raise TypeError("Each row of the matrix must have the same size")
   if type(div) not in (int, float):
       raise TypeError("div must be a number")
   if div == 0:
       raise ZeroDivisionError("division by zero")
   result = []
   for row in matrix:
       new_row = [round(element / div, 2) for element in row]
       result.append(new_row)
   return result
if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")