def solution(num):
	res = num
	if num == 0:
		print(f'This num {res} is not power of 4.')
	else:
		while num != 1:
			if num % 4 != 0:
				print(f'This num {res} is not power of 4.')
				return
			num = num // 4
		print(f'This num {res} is power of 4.')


num = input("Input: ")
solution(int(num))
