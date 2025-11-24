import numpy as np
import math


def cosine_similarity(v1, v2):
    # Implement your code here

    sum_v1 = 0
    sum_v2 = 0
    dot = 0
    for val1, val2 in zip(v1, v2):
        sum_v1 += val1**2
        sum_v2 += val2**2
        dot += val1 * val2
    return round(dot / (math.sqrt(sum_v1) * math.sqrt(sum_v2)), 3)


if __name__ == "__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([2, 4, 6])
    print(cosine_similarity(v1, v2))
