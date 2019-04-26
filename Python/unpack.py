lista = [1,2,3,4]

a, b, c = lista

# a == 1. b == 2. c == 3.
# mesma coisa para tupla (1,2,3)

d, e, _, f = lista		# o terceiro elemento não me interssa

# mesma coisa para strings "abc"  a == a, b == b, c==c

def func(x, y):
	return x**2, y**2
	# o retorno é uma tupla

r1, r2 = func(1,2) 
# r1 == 1. r2 == 4

# def func(x, y = 3) --- y é opcional, com valor default 3