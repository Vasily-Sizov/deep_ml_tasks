import numpy as np


def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    score = 0
    for val_true, val_pred in zip(y_true, y_pred):
        if val_true == val_pred:
            score += 1

    return score / len(y_true)


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 0, 1])
    output = accuracy_score(y_true, y_pred)
    print(output)  # 0.8333333333333334
