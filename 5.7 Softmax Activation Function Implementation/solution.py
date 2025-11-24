import math


def softmax(scores: list[float]) -> list[float]:
    # Your code here
    logits = []
    for value in scores:
        logits.append(math.exp(value))

    sum_logits = sum(logits)
    probabilities = []
    for value in logits:
        probabilities.append(round(value / sum_logits, 4))

    return probabilities


if __name__ == "__main__":
    scores = [1.0, 2.0, 3.0]
    print(softmax(scores))
