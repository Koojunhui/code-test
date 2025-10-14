def solution(s):
    # 길이가 1인 경우 바로 반환
    if len(s) == 1:
        return 1

    min_length = len(s)

    # 단위 길이 1 ~ len(s)//2 까지 시도
    for unit in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:unit]
        count = 1

        # 문자열을 unit 단위로 순회
        for i in range(unit, len(s), unit):
            curr = s[i:i+unit]
            if curr == prev:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = curr
                count = 1

        # 마지막 블록 처리
        compressed += (str(count) + prev) if count > 1 else prev

        # 최소 길이 갱신
        min_length = min(min_length, len(compressed))

    return min_length
