# -----------
# numpy - arrays - Slicing and Indexing
# -----------
import numpy as np

a = np.arange(10,101,10)
# print(a[3:6])
# print(a[::2])

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16],
                   [17, 18, 19,  20]])

# x1 = matrix[3,2]
# print(x1)
# x2 = matrix[ : , 1 ]
# print(x2)
# x3 = matrix[: , 1:3]
# print(x3)
# x4 = matrix[2:4 , 1:3]
# print(x4)
# x5 = matrix[: , ::2]
# print(x5)
# x6 = matrix[: , 1::2]
# print(x6)
# x7 = matrix[: , ::-1]
# print(x7)
# x8 = matrix[ ::-1 , : ]
# print(x8)
# x9 = matrix[ ::-1 , ::-1 ]
# print(x9)