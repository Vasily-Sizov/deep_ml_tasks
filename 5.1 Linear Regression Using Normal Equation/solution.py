"""
Напишите функцию Python, которая выполняет линейную регрессию с использованием нормального уравнения.
Функция должна принимать в качестве входных данных матрицу X (факторы) и вектор y (таргет) и
возвращать коэффициенты линейной регрессионной модели. Округлите ответ до четырех знаков после запятой,
-0,0 является допустимым результатом для округления очень маленького числа.

θ=(X^T X)^-1X^Ty

Example:

Input:
X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]

Output:
[0.0, 1.0]
"""

import numpy as np


def linear_regression_normal_equation(
    X: list[list[float | int]], y: list[float | int]
) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    return np.round(np.linalg.pinv(X.T @ X) @ X.T @ y, 3).tolist()


if __name__ == "__main__":
    X = [[1, 1], [1, 2], [1, 3]]
    y = [1, 2, 3]

    print(linear_regression_normal_equation(X, y))
