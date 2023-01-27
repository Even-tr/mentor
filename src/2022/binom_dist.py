import numpy as np
import matplotlib.pyplot as plt
import math as m

def binom_cof(n, k):
    #Beregner binomialkoefisienten: 'n velger k'
    return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))



def binom_dist(k, p, n):
    # Beregner punktsannsynligheten til binomialfordelingen,
    # altså sannsynligheten for å få k suksesser gitt n uavhengige
    # forsøk, med sannsynliget p.

    # k: antall sksesser
    # p: sannsynlighet for suksess
    # n: antall forsøk

    return binom_cof(n, k)*p**k*(1-p)**(n-k)


n = 100
p = 0.5
xs = np.array(list(range(n+1)))
ys = []
print(xs)

for x in xs:
    ys.append(binom_dist(x,p, n))

plt.plot(xs,ys)
plt.show()


def f(x):
    return np.exp(-x**2)

xs = np.linspace(-3,3,100)
plt.plot(xs, f(xs))
plt.show()