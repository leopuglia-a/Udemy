list1 = [1,2,3,4]
list2 = [5,6,7,8,9]

list3 = list1 + list2

# + representa a união

list1.pop(1) 		# pop(<indice>) pela posição
list1.remove(1) 	# remove(<elemento>) pelo valor

tam = len(list1) 	# tamanho da lista
num = 3

if num in list1:  	# for i in lista: ## in == na lista
	print('elemento encontrado')
else:
	print('elemento não encontrado')

t_lista = tuple(list1) 		# transforma em tupla

list1.append(10)	# adiciona ao final da lista
list1.insert(1,11)	# adiciona 11 na posição 1 insert(<pos>,<elem>)

list1.sort()		# ordena crescentemente

list2[-1]	# ultimo elemento o - é indice ao contrario
list2[1:3]	# 6,7, 8 não pois não inclui [3]
list2[1:]	# 6,7,8,9
list2[::-1]	# inverte a lista