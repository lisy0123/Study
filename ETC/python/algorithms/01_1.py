n = int(input())

def fn(n):
	cnt = 0
	for r in range(n+1):		# 바위 낸 사람 수
		for s in range(n+1-r):	# 가위 낸 사람 수
			p = n - r - s		# 보 낸 사람 수
			all = [r, s, p]
			if all.count(max(all)) == 1:
				cnt += 1
	return (cnt)

print(fn(n))
