import random

print(random.randrange(10))		# 10 é limite superior aberto, 0-9

print(random.randint(1,5))		# random entre intervalo 1-5

lista = [1,2,3,4]

print(random.choice(lista))		# seleciona um elemento aleatorio

random.shuffle(lista)
print(lista)					# embaralha lista

print(random.sample(lista, 2))	# 2 elementos aleatorios de lista

print(random.random())			# entre 0 inclusive e 1 exclusive
print(random.uniform(1,10))		# msma coisa mas com intervalo 1-9.99...
