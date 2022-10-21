import numpy as np
import math

dimension = int(input("Please give the dimension of your square matrix as a digit:"))

print("""Hint: if your matrix is like this:")
1   2
3   4
you have to write the elements of the matrix in a single line and separeted by\
 a space as: 1 2 3 4")
Please write your matrix elements: """)

# user will give the entries in a single line
elements = list(map(int, input().split()))

len_elements = len(elements)

if len_elements != pow(dimension, 2):
    print("Incorrect input! your matrix has %i dimension which leads to %i elements but\
 you gave me %i elemenst" %(dimension, pow(dimension, 2), len_elements))
else:
    # printing the matrix given by the user
    matrix = np.array(elements).reshape(dimension, dimension)

    # infinity norm
    infinity_norm_list = []

    for i in range(dimension):
        row_sum = 0

        for j in range(dimension):
            row_sum += abs(matrix[i][j])
        
        infinity_norm_list.append(row_sum)

    # first norm
    first_norm_list = []

    for i in range(dimension):
        column_sum = 0

        for j in range(dimension):
            column_sum += abs(matrix[j][i])
        
        first_norm_list.append(column_sum)

    # E norm
    elements_sum = 0

    for i in range(dimension):
        for j in range(dimension):
            elements_sum += pow(matrix[i][j], 2)
        
    e_norm = math.sqrt(elements_sum)
    
    # second norm
    tMatrix_matrix = np.dot(matrix.transpose(), matrix)

    b = 0
    c = np.linalg.det(tMatrix_matrix)

    for i in range(dimension):
        b += -tMatrix_matrix[i][i]
    
    landa1 = abs(-b + math.sqrt(pow(b, 2) - (4 * c))) / 2
    landa2 = abs(-b - math.sqrt(pow(b, 2) - (4 * c))) / 2

    second_norm = max(math.sqrt(landa1), math.sqrt(landa2))

    # result
    print("==== RESULT ====")
    print("Infinity norm:", max(infinity_norm_list))
    print("First norm:", max(first_norm_list))
    print("E norm: %.2f" %e_norm)
    print("Second norm: %.2f" %second_norm)
