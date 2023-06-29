# The following program plots use NumPy and Matplotlib to create a graph: y = x^2.
import matplotlib.pyplot as plt
import numpy as np

def squared_values(x):
    return x * x

data = np.arange(100)

"""
for i in range(100):
    output = squared_values(i)
    data.append(output)
"""

print(data)

plt.plot(squared_values(data))
plt.show()