from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    m = len(emoticons)

    # 미리 이모티콘별 할인가격 표를 만들어두면 반복 계산을 줄일 수 있음.
    # discounted[i][k] = i번 이모티콘을 discounts[k]% 할인했을 때의 가격
    discounted = [
        [price * (100 - d) // 100 for d in discounts]
        for price in emoticons
    ]

    best_subs, best_revenue = -1, -1

    # 각 이모티콘에 적용할 할인율 인덱스(0..3)를 곱집합으로 전부 시도
    # 데카르트 곱
    for choice in product(range(4), repeat=m):
        subs, revenue = 0, 0

        # 모든 사용자에 대해 구매/가입 판단
        for min_rate, limit in users:
            spend = 0
            for i, idx in enumerate(choice):
                d = discounts[idx]
                if d >= min_rate:            # 기준 이상 할인된 이모티콘은 구매
                    spend += discounted[i][idx]

            if spend >= limit:               # 한도 이상이면 플러스 가입
                subs += 1
            else:                             # 아니면 매출에 더함
                revenue += spend

        # 가입자 우선, 동률이면 매출 큰 쪽으로 갱신
        if subs > best_subs or (subs == best_subs and revenue > best_revenue):
            best_subs, best_revenue = subs, revenue

    return [best_subs, best_revenue]
