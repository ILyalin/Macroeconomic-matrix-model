import copy
import itertools

from matrix import MatrixObject, Matrix


def build_model(matrix: MatrixObject, num_current_participant: int) -> MatrixObject:
    """Operation of the main algorithm"""
    if (len([True for i in range(matrix.size) if
             matrix.content[num_current_participant][i] == -1]) == matrix.size) and (
            len([True for i in range(matrix.size) if matrix.content[i][num_current_participant] == -1]) == matrix.size):
        return matrix
    else:
        participants = []
        for i in range(matrix.size):
            matrix.content[num_current_participant][i] = -1
            if matrix.content[i][num_current_participant] > 0:
                participants.append(i)
            matrix.content[i][num_current_participant] = -1
        if len(participants) > 0:
            return [build_model(matrix=matrix, num_current_participant=participant) for participant in participants][-1]
        else:
            return matrix


def calculate_tolerance_risk_groups(final_matrix: MatrixObject, participant: int) -> (list, list):
    """Calculation of groups"""
    arr_tol = set()
    for line in final_matrix.content:
        for el in range(len(line)):
            if line[el] != -1:
                arr_tol.add(el)
    arr_risk = set(i for i in range(final_matrix.size) if i != participant - 1 and i not in arr_tol)
    return [t + 1 for t in arr_tol], [r + 1 for r in arr_risk]


def calculate_structural_protection_factor(matrix: MatrixObject):
    number_p_destroy_market = []
    comb = list(itertools.permutations([i + 1 for i in range(matrix.size)]))
    for p_first in range(1, matrix.size + 1):
        f = True
        build_mx = copy.deepcopy(matrix)
        count_p = 1
        build_mx = build_model(matrix=build_mx,
                               num_current_participant=p_first - 1)
        if all(line.count(-1) == build_mx.size for line in build_mx.content):
            number_p_destroy_market.append(count_p)
        else:
            while f:
                arr = []
                for p_second in comb:
                    build_mx_temp = copy.deepcopy(build_mx)
                    count_p = 1
                    for j in range(len(p_second)):
                        if p_second[j] != p_first:
                            count_p += 1
                            build_mx_temp = build_model(matrix=build_mx_temp,
                                                        num_current_participant=p_second[j] - 1)
                            if all(line.count(-1) == build_mx_temp.size for line in build_mx_temp.content):
                                arr.append(count_p)
                                f = False
                                break
            number_p_destroy_market.append(min(arr))

    return min(number_p_destroy_market)
