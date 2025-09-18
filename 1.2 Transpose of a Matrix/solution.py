"""
Напишите функцию на Python, которая вычисляет транспонированную матрицу заданной матрицы.

Example:
Input:
a = [
    [1,2,3],
    [4,5,6]
]

Output:
[[1,4],[2,5],[3,6]]

Reasoning:
Транспонированная матрица получается путем перестановки строк и столбцов.
"""


def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    result = []

    for i in range(0, len(a[0])):
        value = []
        for seq in a:
            value.append(seq[i])
        result.append(value)
    
    return result


if __name__ == "__main__":
    print(transpose_matrix([[1,2,3],[4,5,6]])) # [[1,4],[2,5],[3,6]]