def solution(cap, n, deliveries, pickups):
    i = n - 1  # 배달이 남아 있는 가장 먼 집 인덱스
    j = n - 1  # 수거가 남아 있는 가장 먼 집 인덱스
    answer = 0

    # 뒤쪽의 0들을 미리 걷어내는 헬퍼
    def trim_tail(arr, idx):
        while idx >= 0 and arr[idx] == 0:
            idx -= 1
        return idx

    i = trim_tail(deliveries, i)
    j = trim_tail(pickups, j)

    while i >= 0 or j >= 0:
        # 이번 라운드 왕복할 최장 거리(집 번호는 1부터이므로 +1, 왕복이므로 ×2)
        far = max(i, j) + 1
        answer += far * 2

        # 1) 배달: 뒤에서부터 cap만큼 줄이기
        carry = cap
        while i >= 0 and carry > 0:
            if deliveries[i] <= carry:
                carry -= deliveries[i]
                deliveries[i] = 0
                i -= 1
            else:
                deliveries[i] -= carry
                carry = 0
        i = trim_tail(deliveries, i)

        # 2) 수거: 뒤에서부터 cap만큼 줄이기
        carry = cap
        while j >= 0 and carry > 0:
            if pickups[j] <= carry:
                carry -= pickups[j]
                pickups[j] = 0
                j -= 1
            else:
                pickups[j] -= carry
                carry = 0
        j = trim_tail(pickups, j)

    return answer
