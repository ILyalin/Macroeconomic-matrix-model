from matrix import MatrixObject


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


def calculate_tolerance_risk_groups(final_matrix: MatrixObject) -> (list, list):
    """Calculation of groups"""
    arr_tol = set()
    for line in final_matrix.content:
        for el in range(len(line)):
            if line[el] != -1:
                arr_tol.add(el)
    arr_risk = set(i for i in range(final_matrix.size) if i != final_matrix.participant - 1 and i not in arr_tol)
    return [t + 1 for t in arr_tol], [r + 1 for r in arr_risk]
