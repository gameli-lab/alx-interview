#!/usr/bin/python3

''' A 2d matrix rotation module'''


def rotate_2d_matrix(matrix):
    n = len(matrix)

    ''' Step 1: Transpose the matrix '''
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    ''' step 2: Reverse the matrix'''
    for i in range(n):
        matrix[i].reverse()
