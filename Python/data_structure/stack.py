class Stack:
	def __init__(self):
		self.stack = []
		self.len_stack = 0

	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1

	def pop(self):
		if not self.isEmpty():
			# del self.stack[-1]
			self.stack.pop(-1)
			self.len_stack -= 1
		return None

	def top(self):
		return self.stack[-1]

	def isEmpty(self):
		if self.len_stack == 0:
			return True
		else:
			return False

	def lenght(self):
		return self.len_stack

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.isEmpty())
s.pop()
print(s.top())
print(s.lenght())