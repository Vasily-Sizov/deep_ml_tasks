import numpy as np
import math


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:

    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")
    if y_true.size == 0:
        raise ValueError("Arrays cannot be empty")

    rmse = 0
    for val_true, val_pred in zip(y_true, y_pred):
        rmse += (val_true - val_pred) ** 2

    return round(math.sqrt(rmse / len(y_true)), 3)


if __name__ == "__main__":
    y_true = np.array([3, -0.5, 2, 7])
    y_pred = np.array([2.5, 0.0, 2, 8])
    print(rmse(y_true, y_pred))
