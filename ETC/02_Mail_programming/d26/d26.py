import math

def solution(string):
	nums = list(map(int, string[1:-1].split(",")))
	res = nums[0]
	for x in range(1, len(nums)):
		res = math.gcd(res, nums[x])
	print(res)


string = input("Input: ")
solution(string)
