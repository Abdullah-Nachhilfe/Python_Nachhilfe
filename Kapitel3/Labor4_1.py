import numpy as np
import time

M1 = np.array([[0, 0, 0, 0],
               [2, 0, 0, 4.7],  
              [0, 0, 3.5, 0],
              [2.4, 0, 0, 0]])


M2 = np.zeros((4,4))
M2[1,0] = 2
M2[1,3] = 4.7
M2[2,2] = 3.5
M2[3,0] = 2.4

# # mit numpy dot()
# t1 = time.time()
# for n in range(10000,100000+1,10000):
#     v1 = np.ones(n,)*2 
#     v2 = np.ones(n,)*5 
#     skalar_prod = np.dot(v1,v2)
#     print(skalar_prod)
# t2 = time.time()
# dauer = t2 - t1
# print('Die Zeit für np.dot() ist %.3fs' %dauer)

# # mit for schleife
# t1 = time.time()
# for n in range(10000,100000+1,10000):
#     v1 = np.ones(n,)*2 
#     v2 = np.ones(n,)*5
#     sc = 0
#     for i in range(n):
#         sc += v1[i]*v2[i]
#     print(sc)
# t2 = time.time()
# dauer = t2-t1
# print('Die Zeit für schleife ist %.3fs' %dauer)

M2 = np.array([[1, 0],
               [2, 4],
               [2, 1]])

M3 = np.array([[4, 0],
               [0, 1],
               [2, 0]])

M4 = M3*M2
print(M4)

M4 = np.matmul(np.transpose(M2),M3)
print(M4)