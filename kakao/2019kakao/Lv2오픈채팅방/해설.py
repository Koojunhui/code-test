def solution(record):
    user = {}        # uid별 최신 닉네임 저장
    actions = []     # 출력용 로그 기록

    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]

        # Enter / Change는 닉네임이 함께 옴
        if action in ("Enter", "Change"):
            nickname = parts[2]
            user[uid] = nickname  # uid에 대한 최신 닉네임 갱신

        # 출력 메시지가 필요한 경우만 actions에 저장
        if action == "Enter":
            actions.append((uid, "님이 들어왔습니다."))
        elif action == "Leave":
            actions.append((uid, "님이 나갔습니다."))

    # 실제 메시지 변환 (최종 닉네임 기준)
    result = [user[uid] + message for uid, message in actions]
    return result
