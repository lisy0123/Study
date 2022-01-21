def solution(string):
	string = string[1:-1].split("/")
	lst = []

	for num in string:
		if num == "..":
			lst = lst[:-1]
		elif num != ".":
			lst.append(num)

	lst = "/".join(lst)
	print(f'Output: "{lst}"')


string = input("Input: ")
solution(string)
