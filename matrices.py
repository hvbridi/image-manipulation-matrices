from PIL import Image
import math

def get_shape(matrix1 : list[list[int]]):
    if not isinstance(matrix1, list) or len(matrix1) == 0:
        print('Please insert a non-empty and valid matrix')
        return False
    if not isinstance(matrix1[0], list):
        print('The input must be a 2d list')
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

        
def matrix_addition(matrix1, matrix2):
    if not check_same_shape(matrix1, matrix2):
        print('The matrices need to have the same dimensions')
        return False
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n+matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def matrix_subtraction(matrix1, matrix2):
    if not check_same_shape(matrix1, matrix2):
        print('The matrices need to have the same dimensions')
        return False
    matrix3 = []
    for i_row, row in enumerate(matrix1):
        result_row = []
        for i, n in enumerate(row):
            result_row.append(n-matrix2[i_row][i])
        matrix3.append(result_row)
    return matrix3

def matrix_multiplication(matrix1, matrix2):
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
    for row1 in matrix1:
        new_row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k, n in enumerate(row1):
                element += n * matrix2[k][j]
            new_row.append(element)
        result_matrix.append(new_row)
    return result_matrix

def image_to_matrix(image):
    r=[]
    g=[]
    b=[]
    width, height = image.size
    for y in range(height):
        row_r=[]
        row_g=[]
        row_b=[]
        for x in range(width):
            colors = image.getpixel((x,y))
            red,green,blue = colors
            row_r.append(red)
            row_g.append(green)
            row_b.append(blue)
        r.append(row_r)
        g.append(row_g)
        b.append(row_b)
    return r,g,b



def matrix_to_image(matrix_red,matrix_green,matrix_blue):
    image = Image.new(size=(len(matrix_blue[0]),len(matrix_blue)), mode='RGB')
    for y in range(len(matrix_blue)):
        for x in range(len(matrix_blue[0])):
            pixel_rgb = (matrix_red[y][x],matrix_green[y][x],matrix_blue[y][x])
            image.putpixel((x,y),pixel_rgb)
    return image

def to_grayscale(matrix_red,matrix_green,matrix_blue):
    gray_matrix=[]
    for r_row,g_row,b_row in zip(matrix_red,matrix_green,matrix_blue):
        gray_row=[]
        for r,g,b in zip(r_row,g_row,b_row):
            gray_row.append(round(r*0.2126+g*0.7152+b*0.0722))
        gray_matrix.append(gray_row)
    gray_image = matrix_to_image(gray_matrix,gray_matrix,gray_matrix)
    return gray_matrix, gray_image

def rotate_matrix(matrix1, point, angle_degrees):
    shape1 = get_shape(matrix1)
    if not shape1:
        return False
    
    n_rows1, n_columns1 = shape1
    x_centerPoint, y_centerPoint = point # x = column , y = row
    angle_radian = math.radians(angle_degrees)
    cos1 = math.cos(angle_radian)
    sin1 = math.sin(angle_radian)
    
    result_matrix = []
    for r in range(n_rows1):
        result_matrix.append([0] * n_columns1)
    
    for i in range(n_rows1): #i = row = y
        for j in range(n_columns1): # j = column = x
            # Input point into origin (0,0)
            x = j - x_centerPoint
            y = i - y_centerPoint
            
            # Inverse rotation, reversing the angle to find source point
            source_x = cos1 * x + sin1 * y + x_centerPoint
            source_y = -sin1 * x + cos1 * y + y_centerPoint
            sourceRow = round(source_y)
            sourceColumn = round(source_x)
            
            if 0 <= sourceRow < n_rows1 and 0 <= sourceColumn < n_columns1:
                result_matrix[i][j] = matrix1[sourceRow][sourceColumn]
                
    return result_matrix

def scale_matrix(matrix2, scale_factor):
    if not isinstance(scale_factor, (int, float)) or scale_factor <= 0:
        print("Scale Factor must be positive!")
        return False
    
    shape2 = get_shape(matrix2)
    if not shape2:
        return False
    
    n_rows2 , n_columns2 = shape2
    
    rows2 = int(n_rows2 * scale_factor)
    columns2 = int(n_columns2 * scale_factor)
    
    result_matrix = []
    for i in range(rows2):
        result_row = []
        for j in range(columns2):
            sourceRow = int(i / scale_factor)
            sourceColumn = int(j / scale_factor)
            
            result_row.append(matrix2[sourceRow][sourceColumn])
        result_matrix.append(result_row)
        
    return result_matrix

def skew_matrix(matrix3, skew_x, skew_y):
    if not isinstance(skew_x, (int, float)) or not isinstance(skew_y,(int, float)):
        return False
    
    shape3 = get_shape(matrix3)
    if not shape3:
        return False
    
    n_rows3, n_columns3 = shape3
    
    columns3 = n_columns3 + int(abs(skew_x) * n_rows3)
    rows3 = n_rows3 + int(abs(skew_y) * n_columns3)
    
    result_matrix = []
    for r in range(rows3):
        result_matrix.append([0] * columns3)
    
    for i in range(n_rows3):
        for j in range(n_columns3):
            new_j = j + int(skew_x * i)
            new_i = i + int(skew_y * j)
            
            if 0 <= new_i < rows3 and 0 <= new_j < columns3:
                result_matrix[new_i][new_j] = matrix3[i][j]
        
    return result_matrix


            


def edge_detection(matrix, threshold):
    edge_matrix = []
    vertical_kernel = [[-1,0,1],[-2,0,2],[-1,0,1]]
    horizontal_kernel = [[1,2,1],[0,0,0],[-1,-2,-1]]
    height,width = len(matrix), len(matrix[0])
    padded_matrix = []
    for _ in range(height+2):
        padded_row=[]
        for _ in range(width+2):
            padded_row.append(0)
        padded_matrix.append(padded_row)

    for y in range(height):
        for x in range(width):  
            padded_matrix[y+1][x+1] = matrix[y][x]
    
    for y in range(1,height+1):
        edge_row=[]
        for x in range(1,width+1):
            vertical_value = 0
            horizontal_value = 0
            for i in range(3):
                for j in range(3):
                    vertical_value += vertical_kernel[i][j] * padded_matrix[y+i-1][x+j-1]
                    horizontal_value += horizontal_kernel[i][j] * padded_matrix[y+i-1][x+j-1]
            edge_row.append(0 if vertical_value**2 + horizontal_value**2<threshold**2 else 255)
            #edge_row.append(int(min(255,math.sqrt(vertical_value**2 + horizontal_value**2))))
        edge_matrix.append(edge_row)
    return edge_matrix



#r,g,b = image_to_matrix(Image.open('fat_frog.bmp'))
#image = to_grayscale(r,g,b)[1]

#image.show()






