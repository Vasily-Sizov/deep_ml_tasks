"""
Напишите функцию Python, которая умножает матрицу на скаляр и возвращает результат.
"""


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:

    for seq in matrix:
        for i in range(0, len(seq)):
            seq[i] = seq[i] * scalar

    return matrix


if __name__ == "__main__":

    matrix = [[1, 2], [3, 4]]
    scalar = 2
    print(scalar_multiply(matrix, scalar))  # [[2, 4], [6, 8]]
