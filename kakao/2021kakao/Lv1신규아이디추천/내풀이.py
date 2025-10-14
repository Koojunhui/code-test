import re


def solution(new_id):
    # 모든 대문자 -> 소문자
    new_id = new_id.lower()

    # a~z / 숫자 / - / _ / . 제외한 모든 문자 제거
    new_id = re.sub(r'[^\da-z-_.]', '', new_id)

    # 마침표(.)가 2번 이상 연속 -> 1개
    new_id = re.sub(r'\.{2,}', '.', new_id)

    # 마침표가 처음이나 끝 -> 제거
    new_id = new_id.strip('.')

    # 빈 문자열이면 "a" 대입
    if len(new_id) == 0:
        new_id += "a"

    # 길이가 16 이상이면, 처음부터 15개 문자 제외 나머지 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')

    # 길이가 2 이하이면, 마지막 문자를 길이가 3 될 때까지 끝에 붙임
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id) - 1]

    return new_id