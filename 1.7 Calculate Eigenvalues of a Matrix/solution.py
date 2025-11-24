"""
a-lam d
b c-lam

(a-lam)(c-lam) -bd = 0
ac-a*lam - lam*c + lam^2 -bd = 0
lam^2 -lam*(a+c) + ac-bd = 0

D = (a+c)^2-4(ac-bd)

a1 = ((a+c) + sqrt(D))/2
a1 = ((a+c) - sqrt(D))/2

"""

import math


def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:

    a = matrix[0][0]
    d = matrix[0][1]
    b = matrix[1][0]
    c = matrix[1][1]
    D = (a + c) ** 2 - 4 * (a * c - b * d)
    print(a, b, c, d)
    print(D)
    e1 = ((a + c) + math.sqrt(D)) / 2
    e2 = ((a + c) - math.sqrt(D)) / 2
    return [e1, e2]


if __name__ == "__main__":
    matrix = [[2, 1], [1, 2]]
    print(calculate_eigenvalues(matrix))
