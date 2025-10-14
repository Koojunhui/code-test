from datetime import datetime, timedelta


def solution(lines):
    times = []

    for line in lines:
        # 로그 파싱
        date, time_str, duration_str = line.split()
        end_time = datetime.strptime(date + " " + time_str, "%Y-%m-%d %H:%M:%S.%f")
        duration = float(duration_str[:-1])  # 뒤의 's' 제거
        start_time = end_time - timedelta(seconds=duration) + timedelta(milliseconds=1)

        times.append((start_time, end_time))

    max_count = 0
    for start, end in times:
        # 각 요청의 시작/끝 시각 기준으로 1초 구간 잡기
        intervals = [start, end]
        for point in intervals:
            window_start = point
            window_end = point + timedelta(seconds=1) - timedelta(milliseconds=1)

            count = 0
            for s, e in times:
                # [s, e]와 [window_start, window_end]가 겹치면 count++
                if e >= window_start and s <= window_end:
                    count += 1
            max_count = max(max_count, count)

    return max_count

# .strftime("%H:%M") 출력용 문자열