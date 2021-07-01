n, m = input().split()
n = int(n)
m = int(m)

arr = [[0] * m for i in range(n)]
cnt = 0

for i in range(m-1, -1, -1):
	for j in range(n):
		cnt += 1
		arr[j][i] = cnt

for i in range(n):
	for j in range(m):
		print(arr[i][j], end = " ")
	print()
