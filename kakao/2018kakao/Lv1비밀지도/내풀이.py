import numpy as np


def solution(n, arr1, arr2):
    map_1 = convert_to_binary_matrix(arr1, n)
    map_2 = convert_to_binary_matrix(arr2, n)

    merge_map = get_merge_map(map_1, map_2)
    print_map = get_print_map(merge_map)

    return print_map


def convert_to_binary_matrix(arr, n):
    result = []
    for x in arr:
        binary_str = bin(x)[2:].zfill(n)
        row = [int(bit) for bit in binary_str]
        result.append(row)
    return result


def get_merge_map(map_1, map_2):
    merge_map = (np.array(map_1) + np.array(map_2)).tolist()

    return merge_map


def get_print_map(merge_map):
    print_map = []
    for row in merge_map:
        print_row = ""
        for token in row:
            if token == 0:
                print_row += " "
            else:
                print_row += "#"
        print_map.append(print_row)

    return print_map
