def solution(strings):
	strings = strings.split("],")
	nums, num = strings
	num = int(num) - 1
	nums += "]"
	nums = list(map(int, nums[1:-1].split(",")))

	for i in range(num):
		nums.remove(max(nums))
	print (f'Output: {max(nums)}')

strings = input("Input: ")
solution(strings)
