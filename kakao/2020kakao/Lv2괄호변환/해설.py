def solution(p):
    # 1. 입력이 빈 문자열이면 빈 문자열 반환
    if p == "":
        return ""

    # 2. 문자열 w를 균형잡힌 괄호 문자열 u, v로 분리
    u, v = split_uv(p)

    # 3. u가 올바른 괄호 문자열인지 확인
    if is_correct(u):
        # 3-1. v에 대해 재귀 수행하고 u + v 반환
        return u + solution(v)
    else:
        # 4. u가 올바르지 않으면 다음 과정 수행
        # 4-1 ~ 4-5
        return "(" + solution(v) + ")" + reverse_brackets(u[1:-1])


# 균형잡힌 괄호 문자열 (u, v)로 분리하는 함수
def split_uv(p):
    open_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_count += 1
        else:
            open_count -= 1
        if open_count == 0:  # 균형이 맞는 순간 u, v 분리
            return p[:i+1], p[i+1:]
    return p, ""


# 올바른 괄호 문자열인지 판별하는 함수
def is_correct(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


# 괄호 방향 뒤집기 함수
def reverse_brackets(s):
    return ''.join('(' if ch == ')' else ')' for ch in s)
