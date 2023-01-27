import numpy as np
import matplotlib.pyplot as plt

small = 10**(-10)


def f(x):
    return small*x**10 - small*x**9

def fprime(x):
    return 2*x

xmin = 0
xmax = 0.0000000000001

def differentiate(f, deltax, start = xmin, stop = xmax):
    nsteps = int((stop - start)/deltax)

    xs = np.linspace(start, stop, nsteps)
    tmp = f(xs[1:])
    ys = tmp - f(xs[:-1])
    return ys



plt.plot(differentiate(f, 0.000000000000000000001))
plt.show()