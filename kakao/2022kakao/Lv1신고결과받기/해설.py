def solution(id_list, report, k):
    # 1️⃣ 중복 신고 제거
    report = set(report)

    # 2️⃣ 각 유저별 신고당한 횟수 카운트용 딕셔너리
    reported_count = {user: 0 for user in id_list}

    # 3️⃣ 각 유저가 신고한 대상 기록
    report_map = {user: [] for user in id_list}

    # 4️⃣ 신고 정보 파싱
    for r in report:
        reporter, target = r.split()
        report_map[reporter].append(target)
        reported_count[target] += 1

    # 5️⃣ 정지된 유저 목록 (k번 이상 신고당한 사람)
    suspended = [user for user, cnt in reported_count.items() if cnt >= k]

    # 6️⃣ 메일 횟수 계산
    result = []
    for user in id_list:
        mail_count = sum(1 for target in report_map[user] if target in suspended)
        result.append(mail_count)

    return result
