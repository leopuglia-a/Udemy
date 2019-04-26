class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.queue = []
		self.len_queue = 0

	def push(self, e):
		self.queue.append(e)
		self.len_queue += 1

	def pop(self):
		if self.len_queue != 0:
			self.queue.pop(0)
			self.len_queue -= 1
		else:
			print("None")

	def show(self):
		for i in self.queue:
			print(i)
		if self.len_queue == 0:
			print(None)

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(4)
q.pop()
q.pop()
q.pop()
q.show()