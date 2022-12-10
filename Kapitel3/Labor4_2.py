import numpy as np

# x + y + z = 50,22
# 0.1x + 52.70/100y - z = 0
#  x - y + z*1.1825 = 0

A = np.array([[1, 1, 1],
              [0, -1, 1.18251],
              [0.1, 0.5270, -1]])

# A = np.array([[1, 1, 1],
#               [0, -1, 1.18251],
#               [0, -1, 1.18251]])

x = np.array([50.22, 0, 0])
try:
    lsg = np.linalg.solve(A, x)
except np.linalg.LinAlgError:
    print('Matrix mit det = ',str(np.linalg.det(A)), 'Ist nicht invertierbar')
print('x = %.3f, y =  %.3f, z = %.3f' % (lsg[0], lsg[1], lsg[2]))


