def merge_sort(nums):
	def sort(low, high):
		if high - low < 2:
			return
		mid = (low + high) // 2
		sort(low, mid)
		sort(mid, high)
		merge(low, mid, high)

	def merge(low, mid, high):
		tmp = []
		l, h = low, mid
		while l < mid and h < high:
			if nums[l] < nums[h]:
				tmp.append(nums[l])
				l += 1
			else:
				tmp.append(nums[h])
				h += 1
		while l < mid:
			tmp.append(nums[l])
			l += 1
		while h < high:
			tmp.append(nums[h])
			h += 1
		for i in range(low, high):
			nums[i] = tmp[i - low]

	sort(0, len(nums))
	print("Output:", nums)


def merge_sort_basic(nums):
	if len(nums) < 2:
		return nums

	mid = len(nums) // 2
	low_nums = merge_sort_basic(nums[:mid])
	high_nums = merge_sort_basic(nums[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_nums) and h < len(high_nums):
		if low_nums[l] < high_nums[h]:
			merged_arr.append(low_nums[l])
			l += 1
		else:
			merged_arr.append(high_nums[h])
			h += 1
	merged_arr += low_nums[l:]
	merged_arr += high_nums[h:]
	return merged_arr


def solution(strings):
	nums = list(map(int, strings[1:-1].split(",")))
#	res = merge_sort_basic(nums)
#	print("Output:", res)
	merge_sort(nums)


strings = input("Input: ")
solution(strings)
