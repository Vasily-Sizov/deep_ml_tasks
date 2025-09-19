import numpy as np


def r_squared(y_true, y_pred):

    mean = 0
    for value in y_true:
        mean += value

    mean = mean / len(y_true)
    sse = 0
    sst = 0
    for val_true, val_pred in zip(y_true, y_pred):
        sse += (val_true - val_pred) ** 2
        sst += (val_true - mean) ** 2

    return round(1 - sse / sst, 3)


if __name__ == "__main__":
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
    print(r_squared(y_true, y_pred))
