import re


def solution(p):
    answer = self_repeat(p)

    return answer


def is_correct(p):
    while len(p) > 0:
        tmp = p
        p = p.replace("()", "")
        if tmp == p:
            return False
    return True


def get_uv(p):
    p_str = p.replace("(", "1").replace(")", "0")
    p_list = re.findall(r'\d', p_str)
    end_index = 0
    p_sum = 0
    for i in range(len(p_list)):
        if p_list[i] == "0":
            p_sum -= 1
        else:
            p_sum += 1
        end_index = i
        if p_sum == 0:
            break
    return p[:end_index + 1], p[end_index + 1:]


def self_repeat(p):
    if p == "":
        return ""

    # u, v로 분리
    u, v = get_uv(p)

    # 올바른 괄호 문자열 검증
    if is_correct(u):
        return u + self_repeat(v)
    else:
        empty = "("
        empty += self_repeat(v)
        empty += ")"
        empty += get_reverse(u[1:-1])
        return empty


def get_reverse(p):
    p_str = p.replace("(", "1").replace(")", "0")
    p_reverse = p_str.replace("1", ")").replace("0", "(")
    return p_reverse
