def res(nums, k, tmp, idx):
	idx += 1
	if tmp == (len(nums)):
		return -1
	if nums[tmp] == idx:
		tmp += 1
		return res(nums, k, tmp, idx)
	else:
		return idx


def solution(nums):
	nums = list(map(int, nums[1:-1].split(",")))
	print("Output:", res(sorted(nums), len(nums), 0, 0))


nums = (input("Input: "))
solution(nums)
