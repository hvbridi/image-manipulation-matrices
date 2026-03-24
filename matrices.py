def check_shape(matrix1 : list[list[int]], matrix2 : list[list[int]]):
    if not isinstance(matrix1, list) or not isinstance(matrix2, list) or len(matrix1) == 0 or len(matrix2) == 0:
        print('Please insert a non-empty and valid matrix')
        return
    for row in (matrix1 + matrix2):
        if not isinstance(row, list):
            print('Please insert a valid matrix')
            return
    if len(matrix1[0]) == 0:
        print('Please insert a non-empty matrix')
        return
    n_rows = len(matrix1)
    n_columns = len(matrix1[0])
    for row in matrix1:
        if len(row) != n_columns:
            print('Not a valid matrix')
            return
    if len(matrix2) != n_rows:
        print('The matrices need to have the same shape')
        return
    for row in matrix2:
        if len(row) != n_columns:
            print('The matrices need to have the same shape')
            return
    return True

        
def sum_matrix(matrix1, matrix2):
    if not check_shape(matrix1, matrix2):
        return
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n+matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def sub_matrix(matrix1, matrix2):
    if not check_shape(matrix1, matrix2):
        return
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n-matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3






    


