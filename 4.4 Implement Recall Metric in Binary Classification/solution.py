import numpy as np


def recall(y_true, y_pred):
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

    if TP + FN == 0:
        return 0
    return round(TP / (TP + FN), 3)


if __name__ == "__main__":
    import numpy as np

    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 0, 1])

    print(recall(y_true, y_pred))
