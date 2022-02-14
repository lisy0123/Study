def search(nums, k, tmp):
	if tmp == (len(nums) - 1):
		return -1
	if nums[tmp] == k:
		return tmp
	else:
		tmp += 1
		return search(nums, k, tmp)


def solution(nums):
	nums, k = nums.split("],")
	nums = list(map(int, nums[1:].split(",")))
	k = int(k)
	res = search(nums, k, 0)
	print(f"Output: {res}")


nums = input("Input: ")
solution(nums)
