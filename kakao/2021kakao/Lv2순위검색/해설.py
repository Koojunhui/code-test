from itertools import combinations
from bisect import bisect_left
from collections import defaultdict


def solution(info, query):
    info_dict = generate_info_dict(info)
    parsed_queries = list(map(parse_query, query))

    return list(map(
        lambda q: count_applicants(info_dict.get(q[0], []), q[1]),
        parsed_queries
    ))

def generate_info_dict(info_list):
    """지원자 정보 리스트로부터 가능한 모든 조건 조합 딕셔너리 생성"""
    info_dict = defaultdict(list)

    def add_combinations(info_str):
        tokens = info_str.split()
        conditions, score = tokens[:-1], int(tokens[-1])
        # '-'를 포함한 16가지 조합 생성
        for n in range(5):
            for comb in combinations(range(4), n):
                temp = conditions.copy()
                for idx in comb:
                    temp[idx] = '-'
                key = ' '.join(temp)
                info_dict[key].append(score)

    list(map(add_combinations, info_list))
    # 점수 정렬 (이진 탐색용)
    list(map(lambda k: info_dict[k].sort(), info_dict))
    return info_dict


def parse_query(q):
    """query 문자열을 파싱하여 key와 점수 반환"""
    q = q.replace(" and", "")
    tokens = q.split()
    return ' '.join(tokens[:-1]), int(tokens[-1])


def count_applicants(scores, min_score):
    """이진 탐색으로 min_score 이상인 지원자 수 계산"""
    if not scores:
        return 0
    idx = bisect_left(scores, min_score)
    return len(scores) - idx

