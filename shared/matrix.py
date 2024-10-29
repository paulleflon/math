from copy import deepcopy
from shared.arithmetics import gcd, mult_inverse

def matrix_sum(matrix1, matrix2):
	if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
		return None
	result = deepcopy(matrix1)
	for i in range(len(matrix1)):
		for j in range(len(matrix1[i])):
			result[i][j] += matrix2[i][j]
	return result

def matrix_scalar(matrix, scalar):
	result = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			result[i][j] *= scalar
	return result

def matrix_modulo(matrix, modulo):
	result = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			result[i][j] %= modulo
	return result

def matrix_product(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2):
		raise ValueError('Matrix sizes do not match.')
	result = []
	for i in range(len(matrix1)):
		row = []
		for j in range(len(matrix2[0])):
			s = 0
			for k in range(len(matrix1[0])):
				s += matrix1[i][k] * matrix2[k][j]
			row.append(s)
		result.append(row)
	return result


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

def modular_inverse_matrix(matrix, modulo):
	det = determinant(matrix) % modulo
	g = gcd(det, modulo)
	if g != 1:
		return None
	inverse = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			inverse[j][i] = (mult_inverse(det, modulo) * determinant(minor_matrix(matrix, i, j))%modulo) * (-1)**(i+j) % modulo
	return inverse
