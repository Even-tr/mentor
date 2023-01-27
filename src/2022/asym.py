import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-10,10,1000)

def f(x):
    return (x**2 + 10*x-4)/(x-3)
def asym(x):
    return x + 6
ys = f(xs)


plt.plot(xs, ys)
plt.plot(xs, asym(xs))
plt.ylim([-100, 100])
plt.show()