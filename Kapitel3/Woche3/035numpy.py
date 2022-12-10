# -----------
# numpy - linear Algebra
# -----------
import numpy as np
# x + 2y = 5
# 3x + 4y = 11

A = np.array([[1, 2],
              [3, 4]])
b = np.array([5 ,11])

print('A: %s' % A)
print('b: %s' % b)

result = np.linalg.solve(A, b)

print(result)
