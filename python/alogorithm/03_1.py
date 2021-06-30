N = int(input())

# 자릿수 하나 변환
def conv(n, i, v, x):
	res = ''
	if n == 9:
		res += i + x
	elif n == 4:
		res += i + v
	else:
		res += v * (n // 5)
		n %= 5
		res += i * n
	return (res)

# 로마 숫자로 변환
def roman(n):
	m, n = divmod(n, 1000)
	c, n = divmod(n, 100)
	x, n = divmod(n, 10)
	res = 'M' * m
	res += conv(c, 'C', 'D', 'M')	#100, 500, 1000
	res += conv(x, 'X', 'L', 'C')	#10, 50, 100
	res += conv(n, 'I', 'V', 'X')	#1, 5, 10
	return (res)

cnt = {}
for n in range(1, 4000):
	length = len(roman(n))
	if length in cnt:
		cnt[length] += 1
	else:
		cnt[length] = 1

print(cnt[N])
