def solution(strings):
	if len(strings) == 0 or strings == "[]":
		print ("Error")
		return

	strings = strings[1:-1].split(",")
	lst = strings[0]
	for i in range(0, len(lst)):
		c = lst[i]
		for j in range(1, len(strings)):
			if i == len(strings[j]) or strings[j][i] != c:
				print (f'Output: {i} // "{lst[:i]}"')
				return

	print (f'Output: {len(lst)} // {lst}')
	return

strings = input("Input: ")
solution(strings)
