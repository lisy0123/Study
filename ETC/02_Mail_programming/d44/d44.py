import itertools
from functools import reduce

def solution(num):
	num, k = num.split("],")
	nums = list(map(int, num[1:].split(",")))
	nCr = itertools.combinations(nums, 3)
	for nb in nCr:
		res = reduce(lambda x, y: x+y, nb)
		if int(k) == res:
			print(f"{k} with {nb}")
			return
	print("Can't make", k)


print("Ex) [1,5,32,6,1], 9")
num = input("Input: ")
solution(num)
