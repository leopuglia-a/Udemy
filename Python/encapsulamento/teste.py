class Pessoa:
	"""docstring for Pessoa"""
	def __init__(self, nome):
		self.__nome = __nome	# __ torna privado

	@property
	def nome(self):
		return self.__nome
	
	@nome.setter
	def nome(self, nome):
		self.__nome = nome

p = Pessoa('Marcos')
print(p.nome)
		