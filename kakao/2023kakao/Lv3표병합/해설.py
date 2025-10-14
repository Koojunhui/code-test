def solution(commands):
    N = 50

    # 1-based 인덱스: 51 x 51 배열
    merged = [[(i, j) for j in range(51)] for i in range(51)]  # 대표 좌표
    content = [["EMPTY" for _ in range(51)] for _ in range(51)]  # 대표 좌표에만 실제 값

    def rep(r, c):
        """현재 셀의 대표 좌표 반환: merged[r][c] 값."""
        return merged[r][c]

    def update_cell(r, c, value):
        """UPDATE r c value: 대표 좌표의 값을 value로."""
        x, y = rep(r, c)
        content[x][y] = value

    def update_all(v1, v2):
        """UPDATE value1 value2: content에서 v1인 모든 원소를 v2로."""
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if content[i][j] == v1:
                    content[i][j] = v2

    def merge_cells(r1, c1, r2, c2):
        """MERGE r1 c1 r2 c2: 두 대표를 하나로. 값 규칙 반영."""
        x1, y1 = rep(r1, c1)
        x2, y2 = rep(r2, c2)
        if (x1, y1) == (x2, y2):
            return

        # 병합 후 대표는 (x1, y1)로 통일 (임의 선택, 규칙과 상충 없음)
        # 먼저 병합 대상 두 대표의 기존 값 확보
        v1 = content[x1][y1]
        v2 = content[x2][y2]

        # merged에서 (x2, y2)를 대표로 가진 모든 셀을 (x1, y1)로 바꾼다
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if merged[i][j] == (x2, y2):
                    merged[i][j] = (x1, y1)

        # 값 결정 규칙
        # - 둘 다 값 있으면 (r1, c1) 대표의 값을 유지
        # - 한쪽만 있으면 그 값을 사용
        if v1 != "EMPTY":
            content[x1][y1] = v1
        elif v2 != "EMPTY":
            content[x1][y1] = v2
        else:
            content[x1][y1] = "EMPTY"

        # (x2, y2)는 이제 대표가 아니므로 값 비우기
        content[x2][y2] = "EMPTY"

    def unmerge_cell(r, c):
        """UNMERGE r c: (r,c)가 속한 그룹을 분해하고 (r,c)만 값을 보존."""
        x, y = rep(r, c)
        keep = content[x][y]

        # 해당 그룹 전체를 원복
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if merged[i][j] == (x, y):
                    merged[i][j] = (i, j)
                    content[i][j] = "EMPTY"

        # (r, c)만 값을 복원
        content[r][c] = keep

    answer = []

    for line in commands:
        parts = line.split()

        if parts[0] == "UPDATE":
            if len(parts) == 4:
                # UPDATE r c value
                r, c = int(parts[1]), int(parts[2])
                v = parts[3]
                update_cell(r, c, v)
            else:
                # UPDATE value1 value2
                v1, v2 = parts[1], parts[2]
                if v1 == v2:
                    continue
                update_all(v1, v2)

        elif parts[0] == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:5])
            merge_cells(r1, c1, r2, c2)

        elif parts[0] == "UNMERGE":
            r, c = map(int, parts[1:3])
            unmerge_cell(r, c)

        elif parts[0] == "PRINT":
            r, c = map(int, parts[1:3])
            x, y = rep(r, c)
            ans = content[x][y]
            answer.append(ans if ans != "EMPTY" else "EMPTY")

    return answer
