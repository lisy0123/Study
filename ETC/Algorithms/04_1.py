N = int(input())

def check(num):
	light = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
	cnt = light[num//10] + light[num%10]
	return (cnt)

res = 0
for i in range(24):
	for j in range(60):
		for k in range(60):
			if check(i) + check(j) + check(k) == N:
				res += 1
print(res)
