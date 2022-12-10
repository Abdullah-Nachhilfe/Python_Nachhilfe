# -----------
# matplotlib
# -----------
import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1, 3, 5, 7, 4, 6])
# plt.show()

# plot x^2
# x = np.linspace(-1, 1)
# y = x**2
# plt.plot(x, y)
# plt.grid()
# plt.xlabel('x-values')
# plt.ylabel('x^2')
# plt.title('A plot')
# plt.show()

t = np.linspace(0,5)
y = np.sin(t)
plt.plot(t, y, 'r:', label = 'Original')
plt.plot(t+1,y, 'y--', label = 't + 1')
plt.plot(t+2,y, 'b.-', label = 't + 2')
plt.legend()
plt.title('sin(t) in t')
plt.xlabel('t')
plt.ylabel('sin(t)')
plt.grid()
plt.show()
