def res(lst):
	a, b = 0, 0
	check = 1
	cnt = len(lst) - 1
	y_cnt = len(lst[0]) - 1
	print("Output: ", end="")

	for x in range(len(lst)):
		if x == 0:
			for num in lst[x]:
				print(num, end=" ")
				if num != lst[x][-1]:
					b += 1
		else:
			if check == 1:
				for y in range(cnt):
					a += 1
					print(lst[a][b], end=" ")
				for y in range(y_cnt):
					b -= 1
					print(lst[a][b], end=" ")
			elif check == -1:
				for y in range(cnt):
					a -= 1
					print(lst[a][b], end=" ")
				for y in range(y_cnt):
					b += 1
					print(lst[a][b], end=" ")
			cnt -= 1
			check *= -1
	


def solution():
	print("Input: \n[", end="")
	lst = []
	while True:
		nblst = input()
		if nblst == "":
			break
		nblst = list(map(int, nblst[1:-2].split(",")))
		lst.append(nblst)

	check = 0
	for x in range(len(lst)):
		if x == len(lst) - 1:
			if len(lst[x]) == len(lst[0]):
				check += 1
		elif len(lst[x]) == len(lst[x+1]):
			check += 1
	if check == len(lst):
		res(lst)
	else:
		print("Error")


solution()
