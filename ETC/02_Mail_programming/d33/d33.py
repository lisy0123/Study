import unittest

class Stack:
	def __init__(self):
		self.items = []
		self.max = 3

	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()

	def print_stack(self):
		print(self.items)

	def peek(self):
		return self.items[len(self.items) - 1]

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)
		
	
class Queue:
	def __init__(self):
		self.st1 = Stack()
		self.st2 = Stack()

	def enqueue(self, item):
		self.st1.push(item)

	def dequeue(self):
		if self.st2.is_empty():
			while self.st1.is_empty() is False:
				self.st2.push(self.st1.pop())

		return self.st2.pop()


class MyTests(unittest.TestCase):
	def test(self):
		test = Queue()
		test.enqueue(1)
		test.enqueue(3)
		self.assertEqual(1, test.dequeue())
		test.enqueue(5)
		self.assertEqual(3, test.dequeue())


if __name__ == '__main__':
	unittest.main()
