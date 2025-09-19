"""
Задача: сгенерировать Confusion Matrix
Ваша задача — реализовать функцию confusion_matrix(data), которая генерирует Confusion Matrix для задачи бинарной классификации.
Confusion Matrix предоставляет сводку результатов прогнозирования по задаче классификации, позволяя визуализировать,
сколько точек данных были правильно или неправильно помечены.

Входные данные:

Список списков, где каждый внутренний список представляет пару
[y_true, y_pred] для одного наблюдения. y_true — фактическая метка, а y_pred — прогнозируемая метка.

Выходные данные:
Confusion Matrix

2×2, представленная в виде списка списков.

Example:

Input:
data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]
print(confusion_matrix(data))

Output:
[[1, 1], [2, 1]]
Reasoning:
Confusion Matrix показывает количество истинных положительных, ложных отрицательных,
ложных положительных и истинных отрицательных результатов.


"""

from collections import Counter


def confusion_matrix(data: list[list[int]]) -> list[list[int]]:
    # Implement the function here

    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for value in data:
        if value[0] == 1 and value[1] == 1:
            TP += 1
        if value[0] == 0 and value[1] == 1:
            FP += 1
        if value[0] == 0 and value[1] == 0:
            TN += 1
        if value[0] == 1 and value[1] == 0:
            FN += 1
    return [[TP, FN], [FP, TN]]


if __name__ == "__main__":
    print(confusion_matrix([[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]))
