n, m = input().split()
n = int(n)
m = int(m)

arr = [[0] * m for i in range(n)]
cnt = 0
offset = 1

for i in range(n-1, -1, -1):
	if offset == 1:
		for j in range(m):
			cnt += 1
			arr[i][j] = cnt
		offset = 0
	else:
		for j in range(m-1, -1, -1):
			cnt += 1
			arr[i][j] = cnt
		offset = 1

for i in range(n):
	for j in range(m):
		print(arr[i][j], end = " ")
	print()
