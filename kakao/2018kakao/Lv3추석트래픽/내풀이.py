from datetime import datetime, timedelta

def solution(lines):
    # 끝시간 문자열 리스트
    end_str = [s.split()[1] for s in lines]
    # 끝시간 datetime 리스트
    end_dt = get_end_dt(end_str)

    # 처리시간 문자열 리스트
    dur_str = [s.split()[2] for s in lines]
    # 처리시간 datetime 리스트
    dur_dt = get_dur_dt(dur_str)

    # 시작시간 datetime 리스트
    start_dt = get_start_dt(end_dt, dur_dt)

    # 초당 최대 처리시간 리스트
    tps_list = get_tps(start_dt, end_dt)

    return max(tps_list)


def get_end_dt(end_str):
    end_dt = []
    for str in end_str:
        end_dt.append(datetime.strptime(str, "%H:%M:%S.%f"))
    return end_dt


def get_dur_dt(dur_str):
    dur_dt = []
    for str in dur_str:
        dur_dt.append(timedelta(seconds=float(str[:-1])))
    return dur_dt


def get_start_dt(end_dt, dur_dt):
    start_dt = []
    for i in range(len(end_dt)):
        start_dt.append(end_dt[i] - dur_dt[i] + timedelta(seconds=0.001))
    return start_dt


def get_tps(start_dt, end_dt):
    tps_list = []
    for i in range(len(start_dt)):
        count = 0
        for j in range(i, len(start_dt)):
            if start_dt[i] + timedelta(seconds=0.999) < start_dt[j]:
                break
            elif start_dt[i] + timedelta(seconds=0.999) >= start_dt[j]:
                count += 1
        tps_list.append(count)

    for i in range(len(end_dt)):
        count = 0
        for j in range(i, len(end_dt)):
            if end_dt[i] + timedelta(seconds=0.999) < start_dt[j]:
                break
            elif end_dt[i] + timedelta(seconds=0.999) >= start_dt[j]:
                count += 1
        tps_list.append(count)

    return tps_list