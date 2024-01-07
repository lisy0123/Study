def solution(num):
	num = int(num)

	for nb in range(1, num+1):
		tmp = "1"
		if nb != 1:
			tmp = ""
			res = list(res)
			cnt_nb = res[0]
			cnt = 0

			for n in range(0, len(res)):
				if res[n] == cnt_nb:
					cnt += 1
				else:
					tmp = tmp + str(cnt) + cnt_nb
					cnt_nb = res[n]
					cnt = 1
			tmp = tmp + str(cnt) + cnt_nb
		res = tmp
		print(res)


num = input("Input: ")
solution(num)
