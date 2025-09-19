import numpy as np


def precision(y_true, y_pred):
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
    return TP / (TP + FP)


if __name__ == "__main__":

    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 0, 1])

    result = precision(y_true, y_pred)
    print(result)
