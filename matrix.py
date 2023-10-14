from dataclasses import dataclass

@dataclass()
class MatrixObject:
    content: list[list[int]]
    size: int
    participant: int


class Matrix:

    def input_matrix(self) -> MatrixObject:
        """Entering matrix"""
        size = int(input('Введите размер матрицы: '))
        mx: list[list[int]] = list()

        while True:
            for i in range(size):
                print(f'Введите {i + 1}-ю строку матрицы через пробел: ')
                line = list(map(int, input().split()))
                if len(line) == size:
                    mx.append(line)
                    print(i)
                else:
                    print(
                        '\nНекорректная длина строки, введите значения матрицы построчно, в соответствии с указанными '
                        'размерами!')
                    mx.clear()
                    break
            if len(mx) == size:
                break

        return MatrixObject(
            content=mx,
            size=size,
            participant=int(
                input(
                    'Введите номер участника, выбывшего с рынка (номер строки и столбца должен '
                    'совпадать,\nтк участники '
                    'находятся на главной диагонали): '
                )
            )
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
