from matrix import Matrix, MatrixObject
from algorithm import build_model, calculate_tolerance_risk_groups


def main():
    matrix = Matrix()
    entered_matrix: MatrixObject = matrix.input_matrix()
    final_mx: MatrixObject = build_model(matrix=entered_matrix, num_current_participant=entered_matrix.participant - 1)
    matrix.output_final_mx(final_mx)
    group_tolerance, group_risk = calculate_tolerance_risk_groups(final_matrix=final_mx)
    index_tolerance, index_risk = len(group_tolerance), len(group_risk)
    print(
        f'Группа толерантности: g({entered_matrix.participant}) = {group_tolerance}\n'
        f'Группа риска: r({entered_matrix.participant}) = {group_risk}\n'
        f'Индекс толерантности: Q({entered_matrix.participant}) = {index_tolerance}\n'
        f'Индекс риска:R({entered_matrix.participant}) = {index_risk}'
    )


if __name__ == "__main__":
    main()
