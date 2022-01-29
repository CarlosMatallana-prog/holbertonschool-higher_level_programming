#!/usr/bin/python3
""" 2-matrix_divided """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    type_err = 'matrix must be a matrix (list of lists) of integers/floats'
    size_err = 'Each row of the matrix must have the same size'
    type_err_div = 'div must be a number'
    zero_err_div = 'division by zero'
    div_list = []

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(type_err)
    if type(div) not in (int, float):
        raise TypeError(type_err_div)
    if div == 0:
        raise ZeroDivisionError(zero_err_div)
    for row in matrix:
        div_row = []
        if type(row) is not list or len(row) == 0:
            raise TypeError(type_err)
        elif len(row) != len(matrix[0]):
            raise TypeError(size_err)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(type_err)
            div_row.append(round((item / div), 2))
        div_list.append(div_row)
    return (div_list)
