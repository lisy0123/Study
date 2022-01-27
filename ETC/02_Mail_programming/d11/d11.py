def solution(string):
	string = string.split(",")
	if len(string) > 2:
		print("Error")
		return

	if len(string[0]) == len(string[1]):
		lst = {}
		tmp = 0
		for x in range(len(string[0])):
			if string[0][x] not in lst:
				lst[string[0][x]] = string[1][x]
				tmp += 1
			else:
				if lst[string[0][x]] == string[1][x]:
					tmp += 1
		if tmp == len(string[0]):
			print("Output: True")
		else:
			print("Output: False")
	else:
		print ("Output: False")


string = input("Input: ")
solution(string)
