def fatorial(num):
	if num == 0:
		return 0
	return num * fatorial(num-1)

def test_fatorial():
	assert fatorial(0) == 1