from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_dict = defaultdict(set)
    split_report = list(map(lambda x: x.split(), report))

    for report in split_report:
        reported_dict[report[1]].add(report[0])

    for reported in reported_dict:
        if len(reported_dict[reported]) >= k:
            for reporter in reported_dict[reported]:
                answer[id_list.index(reporter)] += 1

    return answer