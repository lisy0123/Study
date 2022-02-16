from functools import reduce
import copy

def solution(num):
	tmp = []
	for n in range(pow(2, num) - 1):
		tmp.append(int(bin(n)[2:]))
	cptmp = copy.deepcopy(tmp)
	for n in tmp:
		nb = list(str(n))
		idx = 0
		for x in nb:
			if idx == 1:
				if x == "1":
					cptmp.remove(int(reduce(lambda i, j: i+j, nb)))
					break
				else:
					idx = 0
			else:
				if x == "1":
					idx = 1
	print("Output: ", end="")
	for x in cptmp:
		print(f"{x:0{num}d}", end=" ")


num = int(input("Input: "))
solution(num)
