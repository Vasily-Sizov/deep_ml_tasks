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
    """
    X: (m, d), y: (m,) или (m,1), weights: (d,) или (d,1)
    В этой реализации одна 'итерация' = одна ЭПОХА.
    """
    # согласуем формы: 2D-столбцы
    y = y.reshape(-1, 1)  # (m,1)
    w = weights.reshape(-1, 1)  # (d,1)
    m, d = X.shape

    for _ in range(n_iterations):
        if method == "batch":
            # градиент по всей выборке: (2/m) X^T (Xw - y)
            grad = (2.0 / m) * (X.T @ (X @ w - y))  # (d,1)
            w -= learning_rate * grad

        elif method == "stochastic":
            # последовательно по одному объекту (без шифла)
            for i in range(m):
                Xi = X[i : i + 1, :]  # (1,d)
                yi = y[i : i + 1, :]  # (1,1)
                grad = 2.0 * (Xi.T @ (Xi @ w - yi))  # (d,1)
                w -= learning_rate * grad

        elif method == "mini_batch":
            # подряд батчи без шифла; последний батч может быть короче
            for start in range(0, m, batch_size):
                Xb = X[start : start + batch_size, :]  # (b,d)
                yb = y[start : start + batch_size, :]  # (b,1)
                b = Xb.shape[0]
                grad = (2.0 / b) * (Xb.T @ (Xb @ w - yb))  # (d,1)
                w -= learning_rate * grad
        else:
            raise ValueError("method must be 'batch' | 'stochastic' | 'mini_batch'")

    return w.reshape(-1)  # вернуть (d,)
