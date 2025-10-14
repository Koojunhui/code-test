nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 10)
nums.extend([5, 6])
# print(nums)

last_value = nums.pop()
# print(nums)
# print(last_value)

# 인덱스 0의 요소 제거
nums.pop(0)
# print(nums)

# 값이 5인 요소 제거
nums.remove(5)
# print(nums)

# 오름차순 정렬
nums.sort()

# 내림차순 정렬
nums.sort(reverse=True)
# print(nums)

# 리스트 순서 뒤집기
nums.reverse()

# 정렬된 리스트 리턴
sorted_nums = sorted(nums)
# print(sorted_nums)

# 요소의 인덱스 값 구하기
a = sorted_nums.index(4)
# print(a)

# 요소의 개수 구하기
count_4 = sorted_nums.count(4)
# print(count_4)


# ---------- 리스트 컴프리헨션 (가장 많이 씀) ----------
# 1~5 제곱 리스트
squares = [x**2 for x in range(1, 6)]
# print(squares)

# 짝수만 필터링
even_nums = [x for x in range(11) if x % 2 == 0]
print(even_nums)

# 기타 내장함수
max(nums)
min(nums)
sum(nums)

import statistics as stats

# 분산
var = stats.variance(nums)
# 표준편차
std = stats.stdev(nums)