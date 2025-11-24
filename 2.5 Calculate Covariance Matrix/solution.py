"""
Напишите функцию Python для вычисления ковариационной матрицы для заданного набора векторов.
Функция должна принимать список списков, где каждый внутренний список представляет признак с
его наблюдениями, и возвращать ковариационную матрицу в виде списка списков. Кроме того,
предоставьте тестовые примеры для проверки правильности вашей реализации.
"""


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

    result = []
    for candidate1 in vectors:
        covs = []
        for candidate2 in vectors:
            mean1 = sum(candidate1) / len(candidate1)
            mean2 = sum(candidate2) / len(candidate2)
            part_cov = 0.0
            for val1, val2 in zip(candidate1, candidate2):
                part_cov += (val1 - mean1) * (val2 - mean2)
            covs.append(part_cov / (len(candidate2) - 1))
        result.append(covs)
    return result


if __name__ == "__main__":
    print(
        calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]])
    )  # [[1.0, 1.0], [1.0, 1.0]]
