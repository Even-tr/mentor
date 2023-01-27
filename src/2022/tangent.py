# short script which plots takes a function and its
# derivative and returns the tangent function at x1

import numpy as np
import matplotlib.pyplot as plt

x1 = 2

def f(x):
  return x**2 + 100

def fprim(x):
  return 2*x


def tangent(x1, f, fprim):
    a = fprim(x1)
    b = f(x1) - a*x1
    return lambda x: a*x + b

xmin, xmax = -3, 3
xs = np.linspace(xmin,xmax,1000)
ys = f(xs)

dif = abs(ys.max() - ys.min())
ylims = [ys.min() - dif*0.1, ys.max() + dif*0.1]

t = tangent(x1, f, fprim)


  

plt.plot(xs, ys)
plt.plot(xs, t(xs))
plt.ylim(ylims)
plt.show()


from matplotlib.animation import FuncAnimation
#plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax), ylim=ylims)
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line,line2,

def animate(i):
    t = tangent(i, f, fprim)
    y = t(xs)
    line2.set_data(xs, ys)
    line.set_data(xs, y)
    return line, line2,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=xs, interval=10, blit=True)

plt.show()