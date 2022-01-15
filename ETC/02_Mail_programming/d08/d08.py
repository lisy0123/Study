print ("Input Ex) [10,4,3,-1]")
nums = input("Input: ")

nums = list(map(int, nums[1:-1].split(",")))
max_num =  max(nums)
nums.remove(max_num)
lst = []
for num in nums:
	if num != max_num:
		lst.append(num)

try:
	print ("Output:", max(lst))
except:
	print ("Output: Does not exist.")
