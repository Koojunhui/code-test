from itertools import combinations


def solution(orders, course):
    # 모든 메뉴 구성 후보
    all_menu_candidate = get_all_menu_candidate(orders)
    # print(all_menu_candidate)

    # 최소 2명 이상의 손님이 주문한 메뉴
    menu_candidate, menu_count_dict = get_menu_candidate(all_menu_candidate)
    # print(menu_candidate, menu_count_dict)

    # 최종 메뉴 구성
    final_menu = get_final_menu(menu_candidate, menu_count_dict, course)

    # ACE, BCF, ACD

    return final_menu


def get_all_menu_candidate(orders):
    all_menu_candidate = []
    for order in orders:
        comb_list = []
        for i in range(2, len(order) + 1):
            comb_list += list(combinations(order, i))
        all_menu_candidate.append(comb_list)
    all_menu_candidate = [[tuple(sorted(t)) for t in group] for group in all_menu_candidate]
    return all_menu_candidate


def get_menu_candidate(all_menu_candidate):
    menu_candidate = []
    menu_count_dict = {}
    for i in range(len(all_menu_candidate)):
        all_menu = all_menu_candidate[i]
        for j in range(len(all_menu)):
            count = 0
            for k in range(len(all_menu_candidate)):
                if all_menu[j] in all_menu_candidate[k]:
                    count += 1
                    if count >= 2:
                        menu_candidate.append(all_menu[j])
    for menu in menu_candidate:
        menu_count_dict[menu] = menu_candidate.count(menu)
    menu_candidate = set(menu_candidate)
    menu_candidate = list(menu_candidate)
    return menu_candidate, menu_count_dict


def get_final_menu(menu_candidate, menu_count_dict, course):
    final_menu = []
    course_order_count = {}
    course_menu = {}
    for course_num in course:
        course_order_count[course_num] = [0]
    for course_num in course:
        course_menu[course_num] = []

    for i in range(len(menu_candidate)):
        for j in range(len(course)):
            if len(menu_candidate[i]) in course and course_order_count[len(menu_candidate[i])][0] < menu_count_dict[
                menu_candidate[i]]:
                course_order_count[len(menu_candidate[i])] = [menu_count_dict[menu_candidate[i]]]
                course_menu[len(menu_candidate[i])] = [menu_candidate[i]]
            elif len(menu_candidate[i]) in course and course_order_count[len(menu_candidate[i])][0] == menu_count_dict[
                menu_candidate[i]]:
                course_menu[len(menu_candidate[i])].append(menu_candidate[i])

    for course_num in course:
        course_menu[course_num] = set(course_menu[course_num])
        for menu in course_menu[course_num]:
            str = ""
            for token in menu:
                str += token
            final_menu.append(str)

    final_menu = sorted(final_menu)
    return final_menu
