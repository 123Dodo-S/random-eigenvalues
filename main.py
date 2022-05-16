# Declare Constants
NUM = 100000
BINS = 50

# Manage Imports
import numpy as np
import matplotlib.pyplot as plt

# Fix seed for debugging purposes
# np.random.seed(0)

largeEigens = []

for i in range(NUM):
    matrix = (np.random.rand(10, 10) - 0.5) * 100
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    largeEigens.append(np.min(eigenvalues))

# Creates a histogram
plt.hist(largeEigens, bins=BINS)
  
plt.xlabel('Max Eigenvalues')
plt.ylabel('Frequency')

plt.title('Largest Eigenvalues')

# function to show the plot
plt.show()