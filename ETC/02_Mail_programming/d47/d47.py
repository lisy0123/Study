def solution(string):
	string = list(map(int, string[1:-1].split(",")))
	lst = [0, 0, 0]
	for num in string:
		lst[num] += 1
	print("Output: [" + "0 "*lst[0] + "1 "*lst[1] + "2 "*(lst[2]) + "]")


string = input("Input: ")
solution(string)
