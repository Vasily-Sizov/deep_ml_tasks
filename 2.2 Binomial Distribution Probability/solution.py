import math


def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
    successes = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    proba = successes * p**k * (1 - p) ** (n - k)
    return round(proba, 5)


if __name__ == "__main__":
    print(binomial_probability(6, 2, 0.5))
