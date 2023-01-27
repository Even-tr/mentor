import numpy as np
import math as m
import matplotlib.pyplot as plt

x = np.linspace(0,3,1000)

def f(x):
    return 1/np.exp(x)

y = f(x)


plt.plot(x,y)
plt.show()