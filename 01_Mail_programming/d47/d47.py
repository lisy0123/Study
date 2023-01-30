import copy

def solution(string):
	string = list(map(int, string[1:-1].split(",")))
	lst = []
	tmp = copy.deepcopy(string)

	for x in range(len(string)):
		if string[x] == 1:
			tmp.remove(1)
			tmp.append(1)
		elif string[x] == 2:
			tmp.remove(2)
			lst.append(2)
	string = tmp + lst
	print("Output:", string)


string = input("Input: ")
solution(string)
