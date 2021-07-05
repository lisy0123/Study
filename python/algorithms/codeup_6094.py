n = int(input())
s = input().split()

for i in range(n):
	s[i] = int(s[i])

res = s[0]

for i in range(n):
	if s[i] < res:
		res = s[i]

print(res)
