import re
# 닉네임 변경한 기록이 담긴 문자열 배열 record
#       record                      result
# ["Enter uid1234 Muzi",    ["Prodo님이 들어왔습니다.",
# "Enter uid4567 Prodo",    "Ryan님이 들어왔습니다.",
# "Leave uid1234",          "Prodo님이 나갔습니다.",
# "Enter uid1234 Prodo",    "Prodo님이 들어왔습니다."]
# "Change uid4567 Ryan"]
def solution(record):
    split_record = get_split_record(record)
    no_leave_record = get_no_leave_record(split_record)
    no_change_record = get_no_change_record(split_record)
    uid_set = set([uid for _, uid, _ in no_leave_record])
    uid_nickname_list = [[uid, nickname] for _, uid, nickname in no_leave_record]
    finall_uid_nickname_list = get_finall_uid_nickname_list(uid_set, uid_nickname_list)
    finall_uid_nickname_dict = dict(finall_uid_nickname_list)
    patch_split_record = get_patch_split_record(no_change_record, finall_uid_nickname_dict)
    answer = []
    for record in patch_split_record:
        answer.append(record[1] + record[0])

    return answer


def get_split_record(record):
    split_record = []
    for str in record:
        split_record.append(re.split(r' ', str))
    return split_record


def get_no_leave_record(split_record):
    no_leave_record = split_record.copy()
    for record in no_leave_record:
        if record[0] == "Leave":
            no_leave_record.remove(record)
    return no_leave_record


def get_no_change_record(split_record):
    no_change_record = split_record.copy()
    for record in no_change_record:
        if record[0] == "Change":
            no_change_record.remove(record)
    return no_change_record


def get_finall_uid_nickname_list(uid_set, uid_nickname_list):
    finall_uid_nickname_list = []
    for uid in uid_set:
        for uid_nickname in reversed(uid_nickname_list):
            if uid == uid_nickname[0]:
                finall_uid_nickname_list.append(uid_nickname)
                break
    return finall_uid_nickname_list


def get_patch_split_record(split_record, finall_uid_nickname_dict):
    patch_split_record = split_record.copy()
    for record in patch_split_record:
        # 입장/퇴장 매핑
        if record[0] == "Enter":
            record[0] = "들어왔습니다."
        elif record[0] == "Leave":
            record[0] = "나갔습니다."
        # 닉네임 매핑
        record[1] = finall_uid_nickname_dict.get(record[1]) + "님이 "
    return patch_split_record
