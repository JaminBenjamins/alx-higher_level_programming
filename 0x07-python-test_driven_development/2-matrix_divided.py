""" Defining a function for dividing a matrix """


def matrix_divided(matrix, div):
    """Defining a matrix divided by an int or float 
        
        Args:
            matrix - object to be manipulated
            div - element dividing the object

        Exceptions:
            TypeError: if matrix not numeric value
            TypeError: if the rows are not same size
            TypeError: if div is not a number
            ZeroDivisionError: if div is zero

        Return: 
            New matrix
    """
    if not (isinstance(matrix, div) or matrix == [] or
    not all(isinstance(row,list) for row in matrix) or
    not all((isintance(ele, int) or isinstance(ele, float))
            for ele[num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0])) for row in matrix:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(matrix, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    return ([list.map(lambda x : round(x / div, 2), row) for row in matrix
