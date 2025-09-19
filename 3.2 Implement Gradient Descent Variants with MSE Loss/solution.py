"""
В этой задаче вам необходимо реализовать одну функцию, которая может выполнять три варианта
градиентного спуска:
- стохастический градиентный спуск (SGD),
- пакетный градиентный спуск
- и мини-пакетный градиентный спуск с использованием среднеквадратичной ошибки (MSE)
в качестве функции потерь. Функция будет принимать дополнительный параметр для указания,
какой вариант использовать. Примечание: не перемешивайте данные.


"""

import numpy as np


def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray,
    learning_rate: float,
    n_iterations: int,
    batch_size: int = 1,
    method: str = "batch",
) -> np.ndarray:

    rng = np.random.default_rng(seed=42)

    y = y.reshape(-1, 1)
    weights = weights.reshape(-1, 1)
    m, n = X.shape
    for _ in range(0, n_iterations):
        if method == "batch":
            grad = (X.T @ (X @ weights - y)) / m
        elif method == "stochastic":
            index = rng.choice(m)
            X_one = X[index : index + 1, :]
            y_one = y[index : index + 1, :]
            grad = X_one.T @ (X_one @ weights - y_one)
        elif method == "mini_batch":
            indexes = rng.choice(m, size=batch_size, replace=False)
            X_batch = X[indexes]
            y_batch = y[indexes]
            grad = (X_batch.T @ (X_batch @ weights - y_batch)) / batch_size
        else:
            raise ValueError("method must be 'batch' | 'stochastic' | 'mini_batch'")
        weights -= 2 * learning_rate * grad
    return weights.reshape(-1)


if __name__ == "__main__":

    # Sample data
    X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
    y = np.array([2, 3, 4, 5])

    # Parameters
    learning_rate = 0.01
    n_iterations = 1000
    batch_size = 2

    # Initialize weights
    weights = np.zeros(X.shape[1])

    # Test Batch Gradient Descent
    final_weights = gradient_descent(
        X, y, weights, learning_rate, n_iterations, method="batch"
    )

    print(final_weights)
    # Test Stochastic Gradient Descent
    final_weights = gradient_descent(
        X, y, weights, learning_rate, n_iterations, method="stochastic"
    )
    print(final_weights)
    # Test Mini-Batch Gradient Descent
    final_weights = gradient_descent(
        X, y, weights, learning_rate, n_iterations, batch_size, method="mini_batch"
    )
    print(final_weights)
