# Find install and publish python packages with the python package index
import matplotlib.pyplot as plt
import numpy as np

# Input sizes
n = np.linspace(1, 1000, 1000)

# Growth functions
logarithmic = np.log2(n)
linear = n
quadratic = n**2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, logarithmic, label='Logarithmic (O(log n))', color='green')
plt.plot(n, linear, label='Linear (O(n))', color='blue')
# plt.plot(n, quadratic, label='Quadratic (O(n^2))', color='red')

# Labeling
plt.title('Comparing Algorithm Growth Rates')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time')
plt.legend()
plt.grid()
plt.show()