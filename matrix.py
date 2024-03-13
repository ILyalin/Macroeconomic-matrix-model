from dataclasses import dataclass


@dataclass()
class MatrixObject:
    content: list[list[int]]
    size: int
    count_participants: str
    number_significant_el: int


class Matrix:

    def input_matrix(self) -> MatrixObject:
        """Entering matrix"""
        size = int(input('Введите размер матрицы: '))
        mx: list[list[int]] = []
        count_elements = 0
        for _ in range(size):
            mx.append([0] * size)
        print("Далее вводите координаты ненулевых элементов в ввиде: X Y, гдe X - номер строки, Y - номер столбца. Для "
              "прекращения ввода координат, введите 'end'.")
        while True:
            if count_elements < size ** 2:
                print(f'Введите координату ненулевого элемента: ')
                input_strike = input()
                if input_strike == 'end':
                    break
                coordinate_line, coordinate_column = list(map(int, input_strike.split()))
                if 0 <= coordinate_line <= size and 0 <= coordinate_column <= size:
                    mx[coordinate_line - 1][coordinate_column - 1] = 1
                    count_elements += 1
                else:
                    print(
                        'Некорректная координата, продолжайте вводить координаты, в соответствии с указанными '
                        'размерами!')

            else:
                break
        count_participants = input("Введите номер участника, выбывшего с рынка (номер строки и столбца должен "
                                   "совпадать,\nтк участники находятся на главной диагонали, если необходимо "
                                   "отследить всех участников, введите 'all': ")
        return MatrixObject(
            content=mx,
            size=size,
            count_participants=count_participants,
            number_significant_el=count_elements

        )

    def output_final_mx(self, fin_mx: MatrixObject) -> None:
        """Formatted matrix output"""
        compress_mx = []
        for line in fin_mx.content:
            l = [s for s in line if s != -1]
            if len(l) != 0:
                compress_mx.append(l)
        print('Итоговая матрица: ')
        if len(compress_mx) != 0:
            for row in compress_mx:
                for x in row:
                    print("%3d" % x, end=" ")
                print()
        else:
            print([None])
