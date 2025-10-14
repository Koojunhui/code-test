relation = [["100","ryan","music","2"],
 ["200","apeach","math","2"],
 ["300","tube","computer","3"],
 ["400","con","computer","4"],
 ["500","muzi","music","3"],
 ["600","apeach","music","2"]]
# result = 2

from itertools import combinations

def solution(relation):
    n_cols = len(relation[0])
    n_rows = len(relation)
    candidate_keys = []

    # 1) 가능한 모든 컬럼 조합 탐색
    for r in range(1, n_cols + 1):
        for cols in combinations(range(n_cols), r):
            # 2) 유일성 검사
            tmp = [tuple(item[col] for col in cols) for item in relation]
            if len(set(tmp)) == n_rows:
                # 3) 최소성 검사
                if not any(set(cand).issubset(set(cols)) for cand in candidate_keys):
                    candidate_keys.append(cols)

    return len(candidate_keys)


print(solution(relation))