def solution(nums):
	nums = list(map(int, nums[1:-1].split(",")))
	x = 0
	idx = 0
	while True:
		if idx == len(nums) and x == 0:
			print("Output: True")
			return
		if idx > len(nums):
			print("Output:Fasle")
			return
		idx += 1
		x = nums[x]
		print(x)


nums = input("Input: ")
solution(nums)
