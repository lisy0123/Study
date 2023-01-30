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
	nums, k = nums.split(", N=")
	nums = list(map(int, nums.split("->")))
	lst = LinkedList()
	for num in nums:
		lst.append(num)
	k = lst.size() - int(k)

	data = lst.first()
	for x in range(k):
		data = lst.next()
	data = lst.delete()

	print("Output: ", end="")
	data = lst.first()
	if data:
		print(data, end=" ")
		while True:
			data = lst.next()
			if data:
				print(data, end=" ")
			else:
				break
	else:
		print("null")


nums = input("Input: ")
solution(nums)
