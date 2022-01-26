def solution(string):
	nums = list(map(int, string.split(",")))
	num_sum = nums[0]
	res = nums[0]
	
	for x in range(1, len(nums)):
		if nums[x] < num_sum + nums[x]:
			num_sum += nums[x]
		else:
			num_sum = nums[x]
		if res < num_sum:
			res = num_sum
	print("Output:", res)


string = input("Input: ")
solution(string)
