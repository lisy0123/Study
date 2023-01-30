def swap(string, i , j):
	tmp = string
	string = string[:i] + tmp[j] + string[i + 1:]
	string = string[:j] + tmp[i] + string[j + 1:]
	return string


def solution(string, l, r):
	if l == r:
		print (string)
	else:
		for x in range(l, r + 1):
			string = swap(string, l, x)
			solution(string, l + 1, r)
			string = swap(string, l, x)


string = input("Input: ")
solution(string, 0, len(string) - 1)
