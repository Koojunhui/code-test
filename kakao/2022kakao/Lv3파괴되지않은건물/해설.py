def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 1. 스킬 효과 마킹
    for type_, r1, c1, r2, c2, degree in skill:
        val = -degree if type_ == 1 else degree
        diff[r1][c1] += val
        diff[r1][c2 + 1] -= val
        diff[r2 + 1][c1] -= val
        diff[r2 + 1][c2 + 1] += val

    # 2. 가로 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            diff[i][j] += diff[i][j - 1]

    # 3. 세로 누적합
    for j in range(m + 1):
        for i in range(1, n + 1):
            diff[i][j] += diff[i - 1][j]

    # 4. 실제 board에 반영
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                cnt += 1

    return cnt
