import numpy as np


def solution(n, k):
    split = str(np.base_repr(n, base=k)).split('0')

    # 필터링
    split = [x for x in split if x != '' and is_prime(int(x))]

    return len(split)


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):  # 홀수만 검사
        if x % i == 0:
            return False
    return True
