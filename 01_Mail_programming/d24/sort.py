# 선택 정렬
# 주어진 배열에서 가장 작은 원소를 찾아 첫 번째 원소와 교환
# 두 번째 작은 원소를 찾아 두 번째 원소와 교환을 반복하는 정렬하는 방법
# 제자리 정렬 알고리즘: 정렬에 사용되는 추가적인 저장공간 매우 작음
# 불안정적인 정렬: 같은 값은 경우, 순서가 변할 수 있음
# 시간 복잡도: O(N^2)
def select_sort(a: list) -> list:
	n = len(a)
	for i in range(0, n - 1):
		min_idx = i
		for j in range(i + 1, n):
			if a[j] < a[min_idx]:
				min_idx = j
		a[i], a[min_idx] = a[min_idx], a[i]
	return (a)


# 버블 정렬
# 인접한 두 원소 비교, 정렬하는 방법
# 루프를 한번 반복할 때마다 가장 큰 값이 맨 뒤로 이동
# 제자리 정렬 알고리즘
# 안정적인 정렬: 같은 값이어도 정렬 후, 순서 변하지 않음
# 시간 복잡도: O(N^2)
def bubble_sort(a: list) -> list:
	n = len(a)
	for i in range(0, n - 1):
		for j in range(n - i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
	return (a)


# 삽입 정렬
# 자신이 삽입될 위치를 찾아 자리를 만들고 그 위치에 삽입 정렬하는 방법
# 제자리 정렬 알고리즘
# 안정적인 정렬
# 삽입할 때마다 배열의 원소를 이동시켜야 함 => 배열 크기가 큰 경우, 비효율적
# 시간 복잡도: O(N^2)
def insert_sort(a: list) -> list:
	n = len(a)
	for i in range(1, n):
		key = a[i]
		j = i - 1
		while j >= 0 and a[j] > key:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	return (a)


# 셸 정렬
# 삽입 정렬을 보완한 형태의 정렬 방법
# 삽입 정렬이 초기 리스트가 거의 정렬되어있을 때 효율적이라는 점에서 착안
# 멀리 떨어져 있는 원소들을 미리 교환시켜 정렬 속도 향상
# 제자리 정렬 알고리즘
# 불안정적인 정렬
# 시간 복잡도: O(N(logN))~O(N^4/3)
def shell_sort(a: list) -> list:
	h = 1
	n = len(a)
	while h < n:
		h = 3 * h + 1
	h = h // 3
	while h > 0:
		for i in range(h, n):
			k = i - h
			key = a[i]
			while k >= 0 and key < a[k]:
				a[k + h] = a[k]
				k = k - h
			a[k + h] = key
		h = h // 3
	return (a)
