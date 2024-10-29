def gcd(a, b):
	while b:
		a, b = b, a % b
	return a	

def mult_inverse(a, m):
	m0, x0, x1 = m, 0, 1
	while a > 1:
		q = a // m
		m, a = a % m, m
		x0, x1 = x1 - q * x0, x0
	return x1 + m0 if x1 < 0 else x1
