n = int(input())

arr = [[0] * n for i in range(n)]
cnt = 0
offset = 1

for i in range(n):
	if offset == 1:
		for j in range(n):
			cnt += 1
			arr[i][j] = cnt
		offset = 0
	else:
		for j in range(n-1, -1, -1):
			cnt += 1
			arr[i][j] = cnt
		offset = 1

for i in range(n):
	for j in range(n):
		print(arr[i][j], end = " ")
	print()
