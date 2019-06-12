def fat(n):
	if (n == 0):
		return 1
	return n * fat (n - 1)

def fib(n):
	if (n == 1 or n == 2):
		return 1
