def solution(N, stages):
    total_player = len(stages)
    fail_rate = []

    for i in range(1, N + 1):
        not_cleared = stages.count(i)

        if total_player == 0:
            rate = 0
        else:
            rate = not_cleared / total_player

        fail_rate.append((i, rate))

        total_player -= not_cleared
    # print(fail_rate)

    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    # print(fail_rate)

    return [stage for stage, _ in fail_rate]