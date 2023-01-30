def solution(string):
	string = string[1:-1]
	len_str = len(string)
	res = string[0]
	string = string[1:]
	tmp = 0

	while len(res) < len_str and tmp < len_str:
		if res[-1] != string[0]:
			res += string[0]
			tmp = 0
		else:
			string += string[0]
			tmp += 1
		string = string[1:]

	if len(res) != len_str:
		print('Output: ""')
	else:
		print(f'Output: "{res}"')


string = input("Input: ")
solution(string)
