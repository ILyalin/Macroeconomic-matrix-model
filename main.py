import copy

from matrix import Matrix, MatrixObject
from algorithm import build_model, calculate_tolerance_risk_groups, change


def main():
    matrix = Matrix()
    entered_matrix: MatrixObject = matrix.input_matrix()
    count_participants = entered_matrix.count_participants
    if count_participants == "all":
        count_participants = entered_matrix.size
        start = 1
    else:
        count_participants = int(count_participants)
        start = count_participants
    for participant in range(start, count_participants + 1):
        tmp_entered_matrix = copy.deepcopy(entered_matrix)
        final_mx: MatrixObject = build_model(matrix=tmp_entered_matrix,
                                             num_current_participant=participant-1)
        print(f'\nКритерии значимости {participant}-го участника:\n')
        matrix.output_final_mx(final_mx)
        group_tolerance, group_risk = calculate_tolerance_risk_groups(final_matrix=final_mx, participant=participant)
        index_tolerance, index_risk = len(group_tolerance), len(group_risk)
        print(
            f'Группа толерантности: g({participant}) = {group_tolerance}\n'
            f'Группа риска: r({participant}) = {group_risk}\n'
            f'Индекс толерантности: Q({participant}) = {index_tolerance}\n'
            f'Индекс риска:R({participant}) = {index_risk}\n\n'
        )


if __name__ == "__main__":
    main()
