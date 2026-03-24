def check_if_matrix(matrix1 : list[list[int]]):
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
    return True
    
def check_same_shape(matrix1, matrix2):
    if not check_if_matrix(matrix1) or not check_if_matrix(matrix2):
        return False
    n_rows = len(matrix1)
    n_columns = len(matrix1[0])
    for row in matrix1:
        if len(row) != n_columns:
            print('Not a valid matrix')
            return False
    if len(matrix2) != n_rows:
        print('The matrices need to have the same shape')
        return False
    for row in matrix2:
        if len(row) != n_columns:
            print('The matrices need to have the same shape')
            return False
    return True

        
def sum_matrix(matrix1, matrix2):
    if not check_same_shape(matrix1, matrix2):
        return
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






    


