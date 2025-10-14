def solution(today, terms, privacies):
    # 1) 날짜 -> 총 일수로 변환 (모든 달=28일 가정)
    def to_days(ymd: str) -> int:
        y, m, d = map(int, ymd.split('.'))
        return (y * 12 + (m - 1)) * 28 + d  # 월을 0-기반으로 바꿔 곱한 뒤 일 더하기

    today_days = to_days(today)

    # 2) 약관 종류 -> 개월수 매핑
    term_months = {}
    for t in terms:
        k, months = t.split()
        term_months[k] = int(months)

    # 3) 각 개인정보에 대해 파기 여부 판단
    result = []
    for idx, p in enumerate(privacies, start=1):
        date_str, kind = p.split()
        start_days = to_days(date_str)
        expire_start = start_days + term_months[kind] * 28  # 유효기간 다음 날(= 파기 시작일)

        if expire_start <= today_days:  # 오늘이 파기 시작일 이상이면 폐기
            result.append(idx)

    return result


# ---- 예시 테스트 ----
print(solution(
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
))  # [1, 3]

print(solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
))  # [1, 4, 5]
