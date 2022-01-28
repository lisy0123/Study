def solution(strings):
	lst = []
	st = ""
	for x in range(0, len(strings)):
		if strings[x] not in st:
			st += strings[x]
		else:
			lst.append(st)
			st = strings[x]
	lst.append(st)

	print(f'Output: {len(max(lst, key=len))} // "{max(lst, key=len)}"')


strings = input("Input: ")
solution(strings)
