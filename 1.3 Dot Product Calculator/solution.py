"""
Напишите функцию Python для вычисления точечного произведения двух векторов. Функция должна
принимать на вход два одномерных массива NumPy и возвращать точечное произведение в виде одного числа.
"""

import numpy as np


def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
            vec1 (numpy.ndarray): 1D array representing the first vector.
            vec2 (numpy.ndarray): 1D array representing the second vector.
    """

    result = 0
    for val1, val2 in zip(vec1, vec2):
        result += val1 * val2
    return result


if __name__ == "__main__":
    print(calculate_dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])))  # 32
