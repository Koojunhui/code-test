import math
from collections import defaultdict

def time_to_minute(t):
    """HH:MM → 총 분으로 변환"""
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees

    in_time = {}                     # 차량번호 -> 입차시각(분)
    total_time = defaultdict(int)    # 차량번호 -> 누적 주차시간(분)

    for record in records:
        time, car, action = record.split()
        time = time_to_minute(time)

        if action == "IN":
            in_time[car] = time
        else:  # OUT
            total_time[car] += time - in_time[car]
            del in_time[car]

    # 출차 기록이 없는 차량 처리 (23:59 출차로 간주)
    for car, time in in_time.items():
        total_time[car] += time_to_minute("23:59") - time

    # 차량 번호 오름차순 정렬 후 요금 계산
    result = []
    for car in sorted(total_time.keys()):
        t = total_time[car]
        if t <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((t - base_time) / unit_time) * unit_fee
        result.append(fee)

    return result
