from copy import deepcopy

def minor_matrix(matrix, i, j):
	matrix = deepcopy(matrix)
	matrix.pop(i)
	for row in matrix:
		row.pop(j)
	return matrix

def determinant(matrix):
	if len(matrix) != len(matrix[0]):
		return None 
	if len(matrix) == 1:
		return matrix[0][0]
	if len(matrix) == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	det = 0
	for i in range(len(matrix)):
		coef = matrix[0][i] * (1 if i%2 == 0 else -1)
		sub_matrix = minor_matrix(matrix, 0, i)
		det += coef * determinant(sub_matrix)
	return det


def inverse_matrix(matrix):
	det = determinant(matrix)
	if det == 0: 
		return None
	inverse = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			inverse[j][i] = (1/det) * determinant(minor_matrix(matrix, i, j)) * (-1)**(i+j)
	return inverse


print(inverse_matrix([[0,7,2],[5,4,0],[8,0,2]]))
	
