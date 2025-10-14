from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for c in course:
        combs = []
        # 각 주문에 대해 c개씩 조합을 구함
        for order in orders:
            order = ''.join(sorted(order))  # 알파벳 순 정렬
            combs += combinations(order, c)

        # 조합의 빈도수 세기
        counter = Counter(combs)

        if not counter:
            continue

        # 최대 등장 횟수 찾기 (단, 2회 이상만 고려)
        max_count = max(counter.values())
        if max_count < 2:
            continue

        # 가장 많이 등장한 조합을 결과에 추가
        for combo, cnt in counter.items():
            if cnt == max_count:
                result.append(''.join(combo))

    return sorted(result)
