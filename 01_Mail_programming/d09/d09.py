def solution(nums):
	nums = list(map(int, nums[1:-1].split(",")))
	lst = []
	for num in nums:
		if num == 0:
			lst.append(num)
			nums.remove(num)
	nums += lst
	print ("Output:", nums)


print ("Input Ex) [10,4,0,-1,0]")
nums = input("Input: ")
solution(nums)
