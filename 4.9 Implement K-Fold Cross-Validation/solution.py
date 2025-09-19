"""
Реализуйте функцию для генерации разделения на обучающую и тестовую части для K-кратной перекрестной проверки.
Ваша задача состоит в том, чтобы разделить набор данных на k частей и вернуть список индексов обучающей и
тестовой частей для каждой части.

Example:

Input:
k_fold_cross_validation(
    np.array([0,1,2,3,4,5,6,7,8,9]),
    np.array([0,1,2,3,4,5,6,7,8,9]),
    k=5,
    shuffle=False
)

Output:
[
    ([2, 3, 4, 5, 6, 7, 8, 9], [0, 1]),
    ([0, 1, 4, 5, 6, 7, 8, 9], [2, 3]),
    ([0, 1, 2, 3, 6, 7, 8, 9], [4, 5]),
    ([0, 1, 2, 3, 4, 5, 8, 9], [6, 7]),
    ([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])]
"""

import numpy as np


def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """

    idx = list(range(len(X)))

    if shuffle:
        np.random.shuffle(idx)

    size = len(X) // k

    left_bound = 0
    right_bound = size

    indexes = []
    for step in range(0, k):
        if step != k - 1:
            train_idx = idx[:left_bound] + idx[right_bound:]
            test_idx = idx[left_bound:right_bound]
            left_bound += size
            right_bound += size
        else:
            train_idx = idx[:left_bound]
            test_idx = idx[left_bound:]
        indexes.append([train_idx, test_idx])

    result = []
    for pair in indexes:
        result.append((X[pair[0]], X[pair[1]]))
    return result


if __name__ == "__main__":
    print(
        k_fold_cross_validation(
            np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
            np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
            k=5,
            shuffle=False,
        )
    )
