import copy

from matrix import Matrix, MatrixObject
from algorithm import build_model, calculate_tolerance_risk_groups, calculate_structural_protection_factor


def main():
    matrix = Matrix()
    entered_matrix: MatrixObject = matrix.input_matrix()
    participants = entered_matrix.count_participants
    if participants == "all":
        count_participants = entered_matrix.size
        start = 1
    else:
        count_participants = int(participants)
        start = count_participants
    for participant in range(start, count_participants + 1):
        tmp_entered_matrix = copy.deepcopy(entered_matrix)
        final_mx: MatrixObject = build_model(matrix=tmp_entered_matrix,
                                             num_current_participant=participant - 1)
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
    s_p_f = calculate_structural_protection_factor(matrix=entered_matrix) / entered_matrix.size
    s_c = entered_matrix.number_significant_el / (entered_matrix.size ** 2)
    g_q_c = s_p_f * s_c
    print(f'Коэффициент защищенности системы: {s_p_f}')
    print(f'Структурная сложность системы: {s_c}')
    print(f'Общий критерий качества: {g_q_c}')


if __name__ == "__main__":
    main()
