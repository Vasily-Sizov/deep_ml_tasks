import numpy as np


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
        Calculate Mean Absolute Error between two arrays.

        Parameters:
        y_true (numpy.ndarray): Array of true values
    y_pred (numpy.ndarray): Array of predicted values

        Returns:
        float: Mean Absolute Error rounded to 3 decimal places
    """
    mae = 0
    for val_true, val_pred in zip(y_true, y_pred):
        mae += abs(val_true - val_pred)
    return round(mae / len(y_true), 3)


if __name__ == "__main__":
    y_true = np.array([3, -0.5, 2, 7])
    y_pred = np.array([2.5, 0.0, 2, 8])

    print(mae(y_true, y_pred))
