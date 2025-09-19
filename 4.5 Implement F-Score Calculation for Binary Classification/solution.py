import numpy as np


def f_score(y_true: np.ndarray, y_pred: np.ndarray, beta: float) -> float:
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for val_true, val_pred in zip(y_true, y_pred):
        if val_true == 1 and val_pred == 1:
            TP += 1
        if val_true == 0 and val_pred == 0:
            TN += 1
        if val_true == 0 and val_pred == 1:
            FP += 1
        if val_true == 1 and val_pred == 0:
            FN += 1

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    f_measure = (
        (1 + beta * beta) * precision * recall / (beta * beta * precision + recall)
    )
    return round(f_measure, 3)


if __name__ == "__main__":

    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 0, 1])
    beta = 1

    print(f_score(y_true, y_pred, beta))
