def solution(strings):
	strings, num = strings.split(", k = ")
	num = int(num)
	strings = list(map(int, strings[1:-1].split(",")))

	lst = strings[:num]
	strings = strings[num:]
	strings += lst

	print ("Output: ", strings)


strings = input("Input: ")
solution(strings)
