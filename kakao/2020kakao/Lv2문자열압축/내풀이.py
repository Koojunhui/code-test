def solution(s):
    answer_list = []

    if len(s) == 1:
        return 1

    for i in range(1, (len(s) // 2) + 1):
        answer = ''
        count = 1
        for j in range(0, len(s), i):
            if len(s) - j == len(s) % i:
                answer += s[j:]
                break
            if s[j:j + i] == s[j + i:j + 2 * i]:
                count += 1
            else:
                if count == 1:
                    answer += s[j:j + i]
                else:
                    answer += str(count) + s[j:j + i]
                    count = 1
        answer_list.append(len(answer))

    # print(answer_list)
    return min(answer_list)