today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result: [1, 3]

def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        term_list = term.split()
        term_dict[term_list[0]] = term_list[1]
    today_list = today.split('.')
    today_date = (int(today_list[0]) - 2000) * 12 * 28 + (int(today_list[1]) - 1) * 28 + int(today_list[2])

    expiration_list = get_expiration_date(privacies, term_dict)
    # print(expiration_list)
    # print(today_date)

    for i in range(len(expiration_list)):
        if expiration_list[i] <= today_date:
            answer.append(expiration_list.index(expiration_list[i]) + 1)
            expiration_list[i] = -1     # 중복 값 방지(인덱싱)

    return sorted(answer)

def get_expiration_date(privacies, term_dict):
    expiration_list = []
    for privacy in privacies:
        privacy_list = privacy.split()
        privacy_date = privacy_list[0].split('.')
        expiration_date = (int(privacy_date[0]) - 2000) * 12 * 28 + (int(privacy_date[1]) - 1) * 28 + int(privacy_date[2]) + int(term_dict[privacy_list[1]]) * 28
        expiration_list.append(expiration_date)

    return expiration_list

print(solution(today, terms, privacies))