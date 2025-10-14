pairs = [(1, 10), (2, 5), (3, 8)]
# (a, b) 중에 a만 뽑기
result = [a for a, _ in pairs]
# print(result)


scores = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
names = [name for name, _ in scores]
values = [score for _, score in scores]
# (a, b) 각각 리스트로 분리
# print(names)
# print(values)


# 필터링
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 == 1]
# print(even_numbers)
# print(odd_numbers)


# 2차원 리스트 -> 1차원 리스트 변환
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
# print(flat)


# 대문자로 변환
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)