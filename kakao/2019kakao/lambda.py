students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 90},
    {"name": "Charlie", "score": 85}
]

# 점수 내림차순, 점수가 같으면 이름 오름차순
students.sort(key=lambda x: (-x["score"], x["name"]))
# print(students)


stage = [1, 2, 3, 4, 5]
failure_rate = [0.1, 0.2, 0.3, 0.4, 0.4]
list = []
stage_list = []

for i in range(len(stage)):
    list.append((stage[i], failure_rate[i]))

# 실패율 내림차순, 스테이지 번호 오름차순
list.sort(key=lambda x: (-x[1], x[0]))

for i in range(len(list)):
    stage_list.append(list[i][0])
# print(stage_list)


# 절대값 기준 내림차순 정렬
nums = [-10, -5, 0, 2, 9]
nums.sort(key=lambda x: -abs(x))
print(nums)