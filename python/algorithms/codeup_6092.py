n = int(input())
s = input().split()

for i in range(n):
	s[i] = int(s[i])

d = []

for i in range(24):
	d.append(0)

for i in range(n):
	d[s[i]] += 1

for i in range(1, 24):
	print(d[i], end= " ")
