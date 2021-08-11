n = int(input())

def fn(n):
	if n == 0:
		return (0)
	if n == 1:
		return (1)
	return fn(n - 2) + fn(n - 1)

arr = []
for i in range(n*2):
	if fn(i) > n:
		break
	arr.append(fn(i))
print(arr)
