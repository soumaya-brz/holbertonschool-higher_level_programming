#!/usr/bin/python3
"""
This module provides a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    :param matrix: the matrix will be cloned then divided
    :param div: the divider
    """
    if not isinstance(div, (int, float)) or isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        if matrix and len({len(row) for row in matrix}) > 1:
            raise TypeError("Each row of the matrix must have the same size")
        return [[round(subelement / div, 2) for subelement in element]
                for element in matrix]
    except TypeError as error:
        if "row" in str(error):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
