import numpy as np


def solution(board, skill):
    board_array = np.array(board)
    skill_array = np.array(skill)

    for skill in skill_array:
        default_array = np.zeros(board_array.shape, dtype=int)
        default_array[skill[1]:skill[3] + 1, skill[2]:skill[4] + 1] = skill[5]
        if skill[0] == 1:
            board_array -= default_array
        else:
            board_array += default_array

    return np.count_nonzero(board_array > 0)