n = int(input())

# 중복 조합
# n가지 종류에서 중복 허용, r개를 선택하는 방법,
# r개의 무언가를 n-1의 칸막이로(n개의 구역으로) 나누는 배열하는 방법은 일대일 대응

def fn(n):
	cnt = 0
	for l in range(n + 1):				# 1번째, 2번째 구역 나누기
		for r in range(l, n + 1):		# 2번째, 3번째 구역 나누기
			all = [l, r - l, n - r]
			if all.count(max(all)) == 1:
				cnt += 1
	return (cnt)

print(fn(n))
