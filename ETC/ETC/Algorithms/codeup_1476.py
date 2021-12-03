n, m = map(int, input().split())

arr = [[0] * n for i in range(m)]
cnt = 0

for i in range(n+m-1):
	for j in range(m):
		for k in range(n):
			if j + k == i:
				cnt += 1
				arr[j][k] = cnt

for i in range(n):
	for j in range(m):
		print(arr[j][i], end = " ")
	print()
