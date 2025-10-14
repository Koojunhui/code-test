# 후보키 개수 구하기
relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]

from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    candidate_keys = []

    for r in range(1, n_col + 1):
        for cols in combinations(range(n_col), r):
            # 유일성
            tmp = [tuple(item[col]for col in cols) for item in relation]
            if len(set(tmp)) == n_row:
                # 최소성
                if not any(set(cand).issubset(set(cols)) for cand in candidate_keys):
                    candidate_keys.append(cols)

    return len(candidate_keys)

print(solution(relation))