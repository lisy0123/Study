n = int(input())
matrix = [[0] * n for i in range(n)]
cnt = 0
offset = 0
row = n
col = n

while row > 0 and col > 0:
	for i in range(offset, offset + col):
		cnt += 1
		matrix[offset][i] = cnt
	for i in range(offset + 1, offset + row):
		cnt += 1
		matrix[i][offset + col - 1] = cnt
	for i in range(offset + col -2, offset - 1, -1):
		cnt += 1
		matrix[offset + row - 1][i] = cnt
	for i in range(offset + row - 2, offset, -1):
		cnt += 1
		matrix[i][offset] = cnt

	offset += 1
	row -= 2
	col -= 2

for i in range(n):
	for j in range(n):
		print(matrix[i][j], end = ' ')
	print()
