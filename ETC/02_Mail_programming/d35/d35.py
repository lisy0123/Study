def sub(string, l):
	if l == string[l]:
			print(f"Output: {l} // input[{l}] = {l}")
			return
	elif l == len(string):
		return
	else:
		sub(string, l + 1)


def solution(string):
	string = list(map(int, string[1:-1].split(",")))
	sub(string, 0)


string = input("Input: ")
solution(string)
