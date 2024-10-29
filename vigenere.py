from shared.matrix import *
from shared.utils import *
full_alphabet = {
	'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
	'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21,
	'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
	'y': 34, 'z': 35, '.': 36, ',': 37, ':': 38, ';': 39, '?': 40,
	'!': 41, '(': 42, ')': 43, ' ': 44
}
english_alphabet = {chr(i): i - 97 for i in range(97, 123)}
print(english_alphabet)

def decipher(message, A, B, alphabet):
	reverse_alphabet = {v: k for k, v in alphabet.items()}
	print(reverse_alphabet)
	modulo = len(alphabet)
	print(modulo)
	keyA = modular_inverse_matrix(A, modulo)
	keyB = matrix_modulo(matrix_product(matrix_scalar(keyA, -1), B), modulo)
	deciphered = ''
	gram_k = len(B)
	for i in range(0, len(message), gram_k):
		gram = []
		for j in range(gram_k):
			gram.append([alphabet[message[i + j]]])
		dec = matrix_sum(matrix_modulo(matrix_product(keyA, gram), modulo), keyB)
		dec = matrix_modulo(dec, modulo)
		for j in range(gram_k):
			print(dec[j][0])
			deciphered+= reverse_alphabet[dec[j][0]]
	return deciphered

if __name__ == '__main__':
	choice = menu(['Cipher message', 'Decipher message'], 'Choose the desired action')
	alphabet = full_alphabet if menu(['English alphabet (26 letters)', 'Full alphabet (45 characters)'], 'Choose an alphabet') == 2 else english_alphabet
	message = input('Please enter the message:')
	print('Please enter key matrix A')
	A = input_modulo_matrix(len(alphabet))
	print('Please enter key matrix B')
	B = input_modulo_matrix(len(alphabet))
	if len(A) != len(A[0]):
		print('A matrix must be square.')
		exit()
	if len(B[0]) > 1:
		print('B must be a vertical matrix')
		exit()
	if len(B) != len(A):
		print('Height of B must be same as height of A')
		exit()
	if choice == 0:
		pass
	else:
		print(f'Deciphered message: {decipher(message, A, B, alphabet)}')