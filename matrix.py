import numpy as np

x1 = np.arange(16).reshape(4, 4)
print(x1)
x2 = np.transpose(np.arange(4).reshape(1, 4))
print(x2)

y = np.dot(x1, x2)
print(y)

