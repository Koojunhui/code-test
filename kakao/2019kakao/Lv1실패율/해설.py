def solution(N, stages):
    result = []
    total_players = len(stages)  # 전체 사용자 수

    for stage in range(1, N + 1):
        # 해당 스테이지에 머무르고 있는(아직 클리어 못한) 사용자 수
        not_cleared = stages.count(stage)

        # 스테이지에 도달한 사람 수 = 현재 스테이지 이상인 사람 수
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = not_cleared / total_players

        result.append((stage, failure_rate))

        # 다음 스테이지 계산을 위해 스테이지에 머무른 사람 제외
        total_players -= not_cleared

    # 실패율 내림차순, 스테이지 번호 오름차순
    result.sort(key=lambda x: (-x[1], x[0]))

    # 스테이지 번호만 추출해서 반환
    return [stage for stage, _ in result]
