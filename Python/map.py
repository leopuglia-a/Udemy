'''
map é usado quando queremos aplicar
uma função em todos os itens de uma sequencia
'''

lista  = [1,2,3]
m = map(lambda x: x**2, lista)
for i in m:
	print(i)