import numpy as np


a_list = [1, 2, 3, 3, 3, 4, 5]
b_list = [9, 8, 7, 7, 7, 6, 5]
a_arr = np.array(a_list)
b_arr = np.array(b_list)

# 특정 값 개수 구하기
count = np.count_nonzero(a_arr == 3)
# print(count)

# 인덱스로 조회
# print(arr[0])

# 배열 크기
# print(arr.size)

# 벡터화 연산
# print(a_arr + b_arr)
# print(b_arr - a_arr)
c_arr = a_arr ** 2
# print(c_arr)
# print(np.sqrt(c_arr))

# (0,0) ~ (5,5)까지 전체 0으로 초기화
arr = np.zeros((6, 6), dtype=int)

# (0,0) ~ (3,4)까지 4로 채움
arr[0:4, 0:5] = 4

print(arr.size)
print(arr.shape)    # 행 / 렬

arr.astype(int)     # str -> int 전체 값 형변환

words = ["Hello", "World", "!"]
result = "".join(words)
print(result)   # HelloWorld!
