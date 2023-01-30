def solution(string):
	string, num = string.split("], ")
	num = int(num)
	string = list(map(int, string[1:].split(",")))
	if num in string:
		print("Output: true")
	else:
		print("Output: false")


string = input("Input: ")
solution(string)
