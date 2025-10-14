food_times = [3, 1, 2]
k = 5
# result = 1

import heapq

def solution(food_times, k):
    # 모든 음식 시간이 0이면 -1 반환
    if sum(food_times) <= k:
        return -1

    # (음식시간, 음식번호) 형태로 최소 힙 구성
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))

    sum_value = 0       # 지금까지 소비한 총 시간
    previous = 0        # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 현재 남은 음식 개수

    # 남은 시간(k) 안에서 한 층씩 제거
    while hq:
        # 현재 가장 적은 음식 시간
        time = hq[0][0]

        # 현재 레벨의 음식들 모두 제거할 수 있는지 확인
        spend = (time - previous) * length
        if sum_value + spend > k:
            break

        # 먹을 수 있다면 한 레벨 제거
        heapq.heappop(hq)
        sum_value += spend
        length -= 1
        previous = time

    # 남은 음식들을 번호 순서대로 정렬
    result = sorted(hq, key=lambda x: x[1])

    # 남은 시간 k에서 현재까지 소비한 시간 차이만큼 계산
    idx = (k - sum_value) % length
    return result[idx][1]

print(solution(food_times, k))
