from datetime import datetime
import re


#        fees                  records
# (기본)분   원  분  원(추가)
#    [1, 461, 1, 10]       ["00:00 1234 IN"]
def solution(fees, records):
    car_num_list = [re.sub(r'[A-Z]', '', record) for record in records]
    car_time_num_list = [car_num.split() for car_num in car_num_list]
    car_num_set_list = sorted(list(set([time_num[1] for time_num in car_time_num_list])))
    car_time_dict = {}
    total_car_time_dict = {}
    total_car_minute_dict = {}
    result = [0] * len(car_num_set_list)

    for car_num in car_num_set_list:
        car_time_dict[car_num] = []
        total_car_time_dict[car_num] = [datetime(1900, 1, 1, 0, 0)]
        total_car_minute_dict[car_num] = []

    # 출차내역 있는 차량 합계 시간
    for time_num in car_time_num_list:
        if len(car_time_dict[time_num[1]]) == 0:
            car_time_dict[time_num[1]].append(time_num[0])
            continue
        else:
            total_car_time_dict[time_num[1]][0] += datetime.strptime(time_num[0], "%H:%M") - datetime.strptime(
                car_time_dict[time_num[1]][0], "%H:%M")
            car_time_dict[time_num[1]].pop()

    # 출차내역 없는 차량 -> 23:59 출차 처리
    for car_num in car_num_set_list:
        if len(car_time_dict[car_num]) == 1:
            total_car_time_dict[car_num][0] += datetime(1900, 1, 1, 23, 59) - datetime.strptime(
                car_time_dict[car_num][0], "%H:%M")

    # 총 주차 시간 -> 분 단위로 변환
    for car_num in car_num_set_list:
        tmp = total_car_time_dict[car_num][0].strftime("%H:%M").split(':')
        total_min = int(tmp[0]) * 60 + int(tmp[1])
        total_car_minute_dict[car_num].append(total_min)

        # 요금 계산
    for car_num in car_num_set_list:
        if total_car_minute_dict[car_num][0] >= fees[0]:
            result[car_num_set_list.index(car_num)] += fees[1]
            total_car_minute_dict[car_num][0] -= fees[0]
        else:
            result[car_num_set_list.index(car_num)] += fees[1]
            total_car_minute_dict[car_num][0] = 0
        while total_car_minute_dict[car_num][0] > 0:
            if total_car_minute_dict[car_num][0] % fees[2] > 0:
                result[car_num_set_list.index(car_num)] += (total_car_minute_dict[car_num][0] // fees[2] + 1) * fees[3]
                total_car_minute_dict[car_num][0] = 0
            else:
                result[car_num_set_list.index(car_num)] += (total_car_minute_dict[car_num][0] // fees[2]) * fees[3]
                total_car_minute_dict[car_num][0] = 0

    return result