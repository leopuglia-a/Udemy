'''
filter cria um objeto a partir de uma sequencia que satisfaça a função
no caso: x%2
'''

f = filter(lambda x: x%2 == 0, range(10));

print(type(f))

for i in f:
	print(i)