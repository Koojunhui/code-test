import re


def solution(new_id):
    # 1단계: 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 허용되지 않은 문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나로 치환
    new_id = re.sub(r'\.+', '.', new_id)

    # 4단계: 마침표(.)가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열이라면 "a" 대입
    if not new_id:
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 처음 15자만 남기기
    new_id = new_id[:15]
    # 제거 후 끝에 마침표가 있으면 제거
    new_id = new_id.rstrip('.') # lstrip()

    # 7단계: 길이가 2자 이하라면 마지막 문자를 반복해서 길이를 3으로
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
