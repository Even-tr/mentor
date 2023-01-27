import numpy as np
import matplotlib.pyplot as plt

n_samples = 30

def f(x):
    return 2*x +1

def sample(x):
    return f(x) 

xs = np.linspace(-2,2,100)

plt.plot(xs, f(xs))


xs_sample = np.random.normal(loc=0,scale=1, size=n_samples)
ys_sample = f(xs_sample) + np.random.normal(loc=0, scale=1, size=n_samples)
plt.scatter(xs_sample, ys_sample)
plt.scatter(xs_sample, f(xs_sample) + np.random.normal(loc=0, scale=0.1, size=n_samples))
plt.show()


aar = np.array([2015, 2016, 2017, 2018, 2019])
median = np.array([40300, 41200, 42180, 43400, 45000])

plt.scatter(aar, median)



def find_b(x, y):
    temp1 = np.dot(x, y)
    temp2 = np.dot(x, x)
    return temp1/temp2

def find_a(x, y, b):
    x_mean = x.mean()
    return y.mean() - b*x_mean

b = find_b(aar, median)
a = find_a(aar, median, b)
print(a, b)

def line(a, b):
    return lambda x: a + b*x

reg_line = line(a, b)

plt.plot(aar, reg_line(aar))
plt.show()