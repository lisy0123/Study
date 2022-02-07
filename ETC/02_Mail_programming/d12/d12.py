import itertools
from functools import reduce

def solution(string):
	nums = list(map(int, string[1:-1].split(",")))
	lst = list(itertools.combinations(nums, len(nums)-1))[::-1]
	print("Output: [", end="")

	for idx in range(len(lst)):
		res = reduce(lambda x, y: x*y, lst[idx])
		print(res, end="")

		if idx != len(lst)-1:
			print(", ", end="")
	print("]")


string = input("Input: ")
solution(string)
