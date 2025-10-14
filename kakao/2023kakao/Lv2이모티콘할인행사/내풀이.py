users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# result = [1, 5400]

from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    m = len(emoticons)
    discounted = [[price*(100-rate) // 100 for rate in discounts] for price in emoticons]

    best_subs, best_revenue = -1, -1

    # 데카르트 곱
    for choice in product(range(4), repeat=m):
        subs, revenue = 0, 0

        for min_rate, limit in users:
            spend = 0
            for i, idx in enumerate(choice):
                d = discounts[idx]
                if d >= min_rate:
                    spend += discounted[i][idx]

            if spend > limit:
                subs += 1
            else:
                revenue += spend

        if subs > best_subs or (subs == best_subs and revenue > best_revenue):
            best_subs, best_revenue = subs, revenue

    return [best_subs, best_revenue]

print(solution(users, emoticons))