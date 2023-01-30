class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		tmp = Node("tmp")
		self.head = tmp
		self.tail = tmp
		self.current = None
		self.before = None
		self.n_data = 0

	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node
		self.n_data += 1

	def delete(self):
		pop_data = self.current.data
		if self.current == self.tail:
			self.tail = self.before
		self.before.next = self.current.next
		self.current = self.before
		self.n_data -= 1
		return pop_data
	
	def first(self):
		if self.n_data == 0:
			return None
		self.before = self.head
		self.current = self.head.next
		return self.current.data

	def next(self):
		if self.current.next == None:
			return None
		self.before = self.current
		self.current = self.current.next
		return self.current.data

	def size(self):
		return self.n_data


def solution(nums):
	n1, n2 = nums.split(",")
	n1 = list(map(int, n1.split("->")))
	n2 = list(map(int, n2.split("->")))
	lst1 = LinkedList()
	lst2 = LinkedList()
	for num in n1:
		lst1.append(num)
	for num in n2:
		lst2.append(num)

	lst3 = LinkedList()
	lst3.append(lst1.first())
	lst3.append(lst2.first())
	
	for x in range(max(lst1.size(), lst2.size())-1):
		data = lst1.next()
		if data:
			lst3.append(data)
		data = lst2.next()
		if data:
			lst3.append(data)
	
	print("Output: ", end='')
	data = lst3.first()
	if data:
		print(data, end=' ')
		while True:
			data = lst3.next()
			if data:
				print(data, end= ' ')
			else:
				break


nums = input("Input: ")
solution(nums)
