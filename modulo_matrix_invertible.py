import copy
from _utils import input_modulo_matrix, get_int, print_matrix
from extended_euclidean import ee

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
		sub_matrix = copy.deepcopy(matrix)
		sub_matrix.pop(0)
		for j in range(len(matrix) - 1):
			sub_matrix[j].pop(i)
		det += coef * determinant(sub_matrix)
	return det


def is_invertible_modulo(matrix, modulo):
	det = determinant(matrix)
	gcd = ee(det, modulo)[2]
	print(gcd, det)
	return gcd == 1

if __name__ == '__main__':
	mod = get_int('modulo')
	matrix = input_modulo_matrix(mod)
	res = is_invertible_modulo(matrix,mod)
	print_matrix(matrix)
	print(f'This matrix is {"" if res else "not "}invertible modulo {mod}')