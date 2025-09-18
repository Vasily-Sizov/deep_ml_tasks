"""
Напишите функцию на Python, которая вычисляет скалярное произведение матрицы и вектора. 
Функция должна возвращать список, представляющий результирующий вектор, если операция действительна, или -1, если размеры матрицы и вектора несовместимы. 
Матрица (список списков) может быть умножена на вектор (список) только в том случае, если количество столбцов в матрице равно длине вектора. 
Например, для матрицы n x m требуется вектор длины m.

Example:
Input:
a = [[1, 2], [2, 4]], b = [1, 2]

Output:
[5, 10]

Reasoning:
Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; 
Row 2: (1 * 2) + (2 * 4) = 2 + 8 = 10
"""

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> int|list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
    if len(a[0]) != len(b):
        return -1
    result: list[int|float] = []

    for seq in a:
        value = 0
        for i in range(0, len(seq)):
            value += seq[i]*b[i]
        result.append(value)

    return result

if __name__ == "__main__":
    print(matrix_dot_vector([[1, 2], [2, 4]], b = [1, 2]))