"""
В машинном обучении и статистике функция softmax является обобщением логистической функции,
которая преобразует вектор оценок в вероятности. Функция log-softmax является логарифмом функции
softmax и часто используется для обеспечения численной стабильности при вычислении softmax больших чисел.

Имея одномерный массив оценок numpy, реализуйте функцию Python для вычисления log-softmax массива.

Example:

Input:
A = np.array([1, 2, 3])
print(log_softmax(A))

Output:
array([-2.4076, -1.4076, -0.4076])
"""

import numpy as np


def softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    return np.exp(scores) / np.sum(np.exp(scores))


def log_softmax(scores: list) -> np.ndarray:
    # Your code here
    pass


if __name__ == "__main__":
    A = np.array([1, 2, 3])
    print(softmax(A))
    print(softmax(A))
