def get_shape(matrix1 : list[list[int]]):
    #checks if the input contains at least one element and if it is a list
    if not isinstance(matrix1, list) or len(matrix1) == 0:
        print('Please insert a non-empty and valid matrix')
        return False
    #checks if the the input is a 2d matrix
    if not isinstance(matrix1[0], list):
        print('The input must be a 2d list')
        return False
    #checks if every element inside the input is a list (in order to make it a complete 2d matrix)
    for row in (matrix1):
        if not isinstance(row, list):
            print('Please insert a valid matrix')
            return False
    #checks if the first list of the input is empty (for later use)
    if len(matrix1[0]) == 0:
        print('Please insert a non-empty matrix')
        return False
    #sets the number of rows and columns of the matrix for verification
    n_rows = len(matrix1)
    n_columns = len(matrix1[0])
    #iterates through each list in the matrix and checks if the number of elements is the same as n_columns (the lenght of the first list that was set earlier)
    for row in matrix1:
        if len(row) != n_columns:
            print('Not a valid matrix')
            return False

    return n_rows, n_columns
    
def check_same_shape(matrix1, matrix2):
    #gets the shape of both input matrices
    shape1 = get_shape(matrix1)
    shape2 = get_shape(matrix2)
    #verifies if the shapes are valid
    if not shape1 or not shape2:
        return False
    #checks if they have the same number of columns and rows
    n_rows1, n_columns1 = shape1
    n_rows2, n_columns2 = shape2
    if n_rows1 == n_rows2 and n_columns1 == n_columns2:
        return True
    else:
        return False

        
def matrix_addition(matrix1, matrix2):
    #verification to check if the addition is valid
    if not check_same_shape(matrix1, matrix2):
        print('The matrices need to have the same dimensions')
        return False
    matrix3 = []
    #iterates through the lists and indexes of the matrix
    for i_row, row in enumerate(matrix1):
        #creates a new row for the resultant matrix for each row of the original matrices
        result_row = []
        #iterates through the single elements inside the rows
        for i, n in enumerate(row):
            #appends sum of the certain element of matrix1 and the element in the same position in matrix2
            result_row.append(n+matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def matrix_subtraction(matrix1, matrix2):
    #verification to check if the subtraction is valid
    if not check_same_shape(matrix1, matrix2):
        print('The matrices need to have the same dimensions')
        return False
    matrix3 = []
    #iterates through the lists and indexes of the matrix
    for i_row, row in enumerate(matrix1):
        #creates a new row for the resultant matrix for each row of the original matrices
        result_row = []
        for i, n in enumerate(row):
            #appends subtraction of the certain element of matrix1 and the element in the same position in matrix2
            result_row.append(n-matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def matrix_multiplication(matrix1, matrix2):
    #verification to check if the multiplication is valid
    shape1=get_shape(matrix1)
    shape2=get_shape(matrix2)
    if not shape1 or not shape2:
        return False
    n_rows1, n_columns1 = shape1
    n_rows2, n_columns2 = shape2
    if n_columns1 != n_rows2:
        print('The numbers of columns of the first matrix has to be the same as the number os rows of the second matrix')
        return False
    result_matrix = []
    #iterates every row of matrix1 and creates a new row of the resultant matrix for every loop
    for row1 in matrix1:
        new_row = []
        #iterates through each column of matrix2
        for j in range(len(matrix2[0])):
            #creates the variable of the resultant element of a certain coordenate
            element = 0
            #iterates through the index and element in a certain row of matrix1
            for k, n in enumerate(row1):
            #the element is the sum of products of n (the value from matrix1 at row i, column k) with the value in matrix2 at row k, column j. This calculates the result for the resulting cell at coordinate (i, j).
                element += n * matrix2[k][j]
            new_row.append(element)
        result_matrix.append(new_row)
    return result_matrix

def matrix_transpose(matrix1):
    #verification to check if the transposition is valid
    shape1 = get_shape(matrix1)
    if not shape1:
        return False
    
    n_rows1, n_columns1 = shape1
    matrix3 = []
    #iterates through the columns of the original matrix (they will become the rows of the new matrix)
    for col in range(n_columns1):
        newRow = []
        #iterates through the rows of the original matrix
        for row in range(n_rows1):
            #the elements get swaped because of the outer loop being the columns and the inner the rows
            newRow.append(matrix1[row][col])
        matrix3.append(newRow)
        
    return matrix3
        
def scalar_multiplication(matrix1, k):
    #verification to check if the scalar multiplication is valid
    if not isinstance(k, (int, float)):
        print('k needs to be either a integer or a float')
        return False
    shape1 = get_shape(matrix1)
    if not shape1:
        return False
    
    matrix3 = []
    #iterates through each row
    for row in matrix1:
        resultRow = []
        #iterates through each element of a row
        for n in row:
            #append the product of the element and the scalar to the new row of the new matrix
            resultRow.append(n * k)
        matrix3.append(resultRow)
        
    return matrix3

#testing section
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[1, 2, 3], [4, 5, 6]]
    D = [[7, 8], [9, 10], [11, 12]]
    V = [1, 2, 3]

    print(matrix_addition(A, B))
    print(matrix_addition(A, C))
    print(matrix_subtraction(A, B))
    print(matrix_subtraction(A, C))
    print(matrix_multiplication(C, D))
    print(matrix_multiplication(C, A))
    print(matrix_transpose(C))
    print(scalar_multiplication(A, 2))
    print(scalar_multiplication(A, "2"))
    print(get_shape(V))