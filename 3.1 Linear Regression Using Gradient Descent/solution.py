"""
Напишите функцию Python, которая выполняет линейную регрессию с использованием метода градиентного спуска.
Функция должна принимать в качестве входных данных массивы NumPy
X (фичи с колонкой единиц для intercept) и y (таргет), а также скорость обучения альфа и количество итераций,
и возвращать коэффициенты линейной регрессионной модели в виде массива NumPy.
Округлите ответ до четырех знаков после запятой. -0,0 является допустимым результатом для округления очень маленького числа.

Example:

Input:
X = np.array([[1, 1], [1, 2], [1, 3]]),
y = np.array([1, 2, 3]),
alpha = 0.01,
iterations = 1000

Output:
np.array([0.1107, 0.9513])

Reasoning:
The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization.

Если MSE, то градиент: 1/m X^T(Xw-y)
"""

import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:
    # Your code here, make sure to round
    m, n = X.shape
    w = np.zeros((n, 1))
    y = y.reshape(-1, 1)

    for _ in range(0, iterations):
        grad = (X.T @ (X @ w - y)) / m
        w -= alpha * grad

    return w


if __name__ == "__main__":
    print(
        linear_regression_gradient_descent(
            X=np.array([[1, 1], [1, 2], [1, 3]]),
            y=np.array([1, 2, 3]),
            alpha=0.01,
            iterations=1000,
        )
    )
