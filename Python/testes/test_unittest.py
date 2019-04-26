import unittest

def fat(n):
	if (n == 0):
		return 1
	return n *fat (n-1)

def pot(base, exp):
	if (exp == 0):
		return 1
	return base * pot(base, exp - 1)

def area_quad(lado):
	return lado*lado


class TestMathMethods(unittest.TestCase):
	"""docstring for TestMathMethods"""
	
	def test_pot(self):

		self.assertEqual(1024, pot(2,10))	# verifica por um resultado esperado (1024) para pot(2,10)

unittest.main()