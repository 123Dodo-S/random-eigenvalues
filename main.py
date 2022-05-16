import numpy as np

# Fix seed for debugging purposes
# np.random.seed(0)

matrix = np.random.rand(10, 10)

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print(np.max(eigenvalues))
