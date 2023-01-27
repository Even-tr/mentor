from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

with open ('data/co2_mm.txt') as file:
    aar = []
    co2 = []
    for line in file.readlines():
        tmp = [float(i) for i in line.split()]
        aar.append(tmp[2])
        co2.append(tmp[3])

n = len(aar)
x = np.array(aar)
y = np.array(co2)



def func(t, a,b,c,d, e):
    return a*np.exp(b*t) + c*np.sin(2+np.pi*t + d)**2 + e

offset = 2015

[a,b,c,d, e] = curve_fit(func, x - offset, y)[0]
plt.plot(x, y, '.')

t= np.linspace(x[0], x[-1], 5000) - offset
plt.plot(t+offset, func(t,a,b,c,d,e))

def exponential(t, a, b, c, e):
    return a*np.exp(b*t) + e + c/2

plt.plot(t+offset, exponential(t,a,b,c,e))
plt.show()
