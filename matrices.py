from PIL import Image
import numpy as np
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

'''
def rotate_matrix(matrix,point,degrees):
    new_matrix=[]
    height,width = len(matrix),len(matrix[0])
    for y in range(height):
        blank_row=[]
        for x in range(width):
            blank_row.append(0)
        new_matrix.append(blank_row)

    sin = np.sin(np.deg2rad(degrees))
    cos = np.cos(np.deg2rad(degrees))
    center_x,center_y=point
    rotation_matrix = [[cos,-sin],[sin,cos]]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            moved_x = x-center_x
            moved_y = y-center_y
            result=matrix_multiplication(rotation_matrix,[[moved_x],[moved_y]])
            new_matrix[]


            
        new_matrix.append(new_row)
'''

            


def edge_detection(matrix):
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
            edge_row.append(int(min(255,math.sqrt(vertical_value**2 + horizontal_value**2))))
        edge_matrix.append(edge_row)
    return edge_matrix



r,g,b = image_to_matrix(Image.open('fat_frog.bmp'))
image = to_grayscale(r,g,b)[1]

image.show()

img = Image.open('frog_white_background.bmp')
r2,g2,b2 = image_to_matrix(img)
img = to_grayscale(r2,g2,b2)[0]
img = edge_detection(img)
img = matrix_to_image(img,img,img)
img.show()
img.save('frog_outline.png')


