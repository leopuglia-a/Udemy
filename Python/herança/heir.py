class Transporte:
	"""docstring for Transporte"""
	def __init__(self, nome, peso, preco):
		self.nome = nome
		self.peso = peso
		self.preco = preco

	def getNome(self):
		return self.nome

	def getPeso(self):
		return self.peso

	def getPreco(self):
		return self.preco

class Carro(Transporte):
	"""docstring for carro"""
	def __init__(self, nome, peso, preco, seguro):
		Transporte.__init__(self, nome, peso, preco)
		self.seguro = seguro

	def getSeguro(self):
		return self.seguro
		


carro = Carro('Fusca', 500, 3500, 800)

print(carro.getNome())
print(carro.getPeso())
print(carro.getPreco())
print(carro.getSeguro())	