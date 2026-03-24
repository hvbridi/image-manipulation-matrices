def get_shape(matrix1 : list[list[int]]):
    if not isinstance(matrix1, list) or len(matrix1) == 0:
        print('Please insert a non-empty and valid matrix')
        return False
    for row in (matrix1):
        if not isinstance(row, list):
            print('Please insert a valid matrix')
            return False
        
    if len(matrix1[0]) == 0:
        print('Please insert a non-empty matrix')
        return False
    
    n_rows = len(matrix1)
    n_columns = len(matrix1[0])
    for row in matrix1:
        if len(row) != n_columns:
            print('Not a valid matrix')
            return False

    return n_rows, n_columns
    
def check_same_shape(matrix1, matrix2):
    shape1 = get_shape(matrix1)
    shape2 = get_shape(matrix2)
    if not shape1 or not shape2:
        return False
    n_rows1, n_columns1 = shape1
    n_rows2, n_columns2 = shape2
    if n_rows1 == n_rows2 and n_columns1 == n_columns2:
        return True
    else:
        return False

        
def sum_matrix(matrix1, matrix2):
    if not check_same_shape(matrix1, matrix2):
        return False
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n+matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def sub_matrix(matrix1, matrix2):
    if not check_same_shape(matrix1, matrix2):
        return
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n-matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def mult_matrix(matrix1, matrix2):
    if not get_shape(matrix1) or not get_shape(matrix2):
        return False
    





    


