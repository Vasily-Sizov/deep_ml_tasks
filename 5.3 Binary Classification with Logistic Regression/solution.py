"""
Реализуйте функцию прогнозирования для бинарной классификации с использованием логистической регрессии.
Ваша задача состоит в том, чтобы вычислить вероятности классов с помощью сигмоидной функции и
вернуть бинарные прогнозы на основе порогового значения 0,5.

Example:

Input:
predict_logistic(np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]]), np.array([1, 1]), 0)

Output:
[1 1 0 0]
"""

import numpy as np


def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    """
    Implements binary classification prediction using Logistic Regression.

    Args:
            X: Input feature matrix (shape: N x D)
            weights: Model weights (shape: D)
            bias: Model bias

    Returns:
            Binary predictions (0 or 1)
    """
    # Your code here
    logits = X @ weights + bias
    logits = 1 / (1 + np.exp(-logits))
    return np.where(logits >= 0.5, 1, 0)


if __name__ == "__main__":
    print(
        predict_logistic(
            np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]]), np.array([1, 1]), 0
        )
    )
