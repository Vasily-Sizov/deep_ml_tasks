"""
Напишите функцию Python для вычисления вероятности наблюдения ровно k событий
в фиксированном интервале времени по формуле распределения Пуассона.
Функция должна принимать в качестве входных данных k (количество событий) и
lam (средняя частота появления событий) и возвращать вероятность, округленную до 5 знаков после запятой.

P(k;λ)= λ^k*e^−λ/k!
"""

import math


def poisson_probability(k, lam):
    """
    Calculate the probability of observing exactly k events in a fixed interval,
    given the mean rate of events lam, using the Poisson distribution formula.
    :param k: Number of events (non-negative integer)
    :param lam: The average rate (mean) of occurrences in a fixed interval
    """
    proba = lam**k * math.exp(-lam) / math.factorial(k)
    return round(proba, 5)


if __name__ == "__main__":
    print(poisson_probability(3, 5))  # 0.14037
