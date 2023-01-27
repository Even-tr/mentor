from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def exp(x, l):
    return l*np.exp(-x*l)

xs = np.linspace(0, 10, 10000)
dx = xs[1] - xs[0]
plt.plot(xs, exp(xs, 1), label = 'l = 1')
plt.plot(xs, exp(xs, 2), label = 'l = 2')
plt.plot(xs, exp(xs, 0.5), label = 'l = 0.5')
plt.legend()
plt.show()
print(dx*(exp(xs, 2)).sum())
