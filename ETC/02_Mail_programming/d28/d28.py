def solution(nums):
	nums = sorted(list(map(int, nums[1:-1].split(","))))
	res = 1
	for x in nums:
		if x > res:
			break
		else:
			res += x
	print(f"Output: {res}")


nums = input("Input: ")
solution(nums)
