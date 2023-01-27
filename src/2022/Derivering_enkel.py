"""
Dette programmet viser hvordan man kan enkelt derivere en
funksjon
"""

import matplotlib.pyplot as plt

# funksjoen som skal deriveres
def f(x):
    return x**3 + x + 4

# den analytisk deriverte
def g(x):
    return 3*x**2 + 1

# Lager x verider for plotting etc.
xs = []
for i in range(20):
    xs.append(float(i)/10)

# har x-er, trenger y-er
fys = []
for x in xs:
    fys.append(f(x))

gys = []
for x in xs:
    gys.append(g(x))


#deriverer numerisk:
deltax = xs[1] - xs[0]
print('delta x: ', deltax)
derivert = []
for i in range(len(fys)-1):
    derivert.append((fys[i+1] - fys[i])/deltax)


# plotter resultatene
plt.plot(xs, fys, label='f')
plt.plot(xs[:-1], derivert, label = 'derivert numerisk')
plt.plot(xs, gys, label='derivert analytisk')
plt.legend() # legger til navn i plottet
plt.show() # viser faktisk plottet, ellers er det usynlig
