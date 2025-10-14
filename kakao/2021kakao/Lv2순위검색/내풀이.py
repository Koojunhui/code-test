import numpy as np


# info
# 개발 언어: [cpp, java, python] 중 하나
# 직군: [backend, frontend] ""
# 경력: [junior, senior] ""
# 소울푸드: [chicken, pizza] ""
# 점수: 1 이상 100,000 이하 자연수

# query
# "-" -> 해당 조건 고려 안함
# X점 이상 받은 사람 수

def solution(info, query):
    info_list = []
    query_list = []
    for member in info:
        info_list.append(member.split())
    for restrict in query:
        query_list.append(restrict.replace(" and ", " ").split())

    info_array = np.array(info_list)
    query_array = np.array(query_list)

    answer_list = count_satisfy(info_array, query_array)

    return answer_list


def count_satisfy(info_array, query_array):
    answer_list = []
    answer_dict = {}
    for n in range(len(query_array)):
        answer_dict[n] = 0

    for i in range(len(info_array)):
        for j in range(len(query_array)):
            for k in range(5):
                if query_array[j][k] == "-":
                    continue
                elif k == 4:
                    if int(info_array[i][-1]) >= int(query_array[j][k]):
                        answer_dict[j] += 1
                elif np.count_nonzero(info_array[i] == query_array[j][k]) == 1:
                    continue
                else:
                    break

    for n in range(len(answer_dict)):
        answer_list.append(answer_dict[n])

    return answer_list