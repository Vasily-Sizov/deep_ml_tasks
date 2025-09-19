import numpy as np

X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
y = np.array([2, 3, 4, 5])

weights = np.zeros(X.shape[1])


print(X.shape, weights.shape, y.shape)

print(X.shape, weights.reshape(-1, 1).shape, y.reshape(-1, 1).shape)
