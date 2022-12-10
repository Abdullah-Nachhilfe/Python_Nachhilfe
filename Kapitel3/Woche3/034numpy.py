# -----------
# numpy - random numbers
# -----------
import numpy as np

# matrix = np.random.rand(5,5)*5
# print(matrix)

# matrix2 = np.random.rand(5,5)*5 + 5
# print(matrix2)
matrix3 = np.random.randn(1000, 1000)
# print("Matrix with random numbers in shape %s:\n %s" % (matrix3.shape, matrix3))
# print('Mean = %.2f' % matrix3.mean())
# print('Std = %.2f' % matrix3.std())

matrix3 = np.random.randn(1000, 1000)*2 + 5
print("Matrix with random numbers in shape %s:\n %s" % (matrix3.shape, matrix3))
print('Mean = %.2f' % matrix3.mean())
print('Std = %.2f' % matrix3.std())


