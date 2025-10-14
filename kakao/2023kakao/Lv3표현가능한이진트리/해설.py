def solution(numbers):
    def next_full_len(x_len: int) -> int:
        # 길이가 2^h - 1 이상이 되도록 최소 h를 찾아 반환
        size = 1
        while size < x_len:
            size = size * 2 + 1
        return size

    def can_represent(bin_str: str) -> bool:
        # bin_str는 길이가 2^h - 1인, 중위 순회 배열 관점의 서브트리 구간
        # 규칙: 부모가 0이면 이 구간 전체에 1이 있으면 안 됨
        if len(bin_str) == 1:
            return True
        mid = len(bin_str) // 2
        root = bin_str[mid]
        if root == '0':
            # 부모가 더미면 이 서브트리 어디에도 1이 나오면 안 됨
            return bin_str.count('1') == 0
        # 부모가 1이면 좌/우 서브트리 각각 재귀 확인
        left = bin_str[:mid]
        right = bin_str[mid+1:]
        return can_represent(left) and can_represent(right)

    ans = []
    for n in numbers:
        b = bin(n)[2:]                 # 이진수 문자열
        full_len = next_full_len(len(b))
        b = b.zfill(full_len)          # 앞쪽 0으로 포화 트리 길이 맞추기
        ans.append(1 if can_represent(b) else 0)
    return ans
