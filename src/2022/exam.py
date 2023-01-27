import math as m
from traceback import print_tb
import numpy as np

def f(x):
    return x/(1+x**2)

h = 0.1
x = 0

while (f(x+h) - f(x))/h > 0:
    x = x + 1

#print('x=', x)
def opg1():
    rentefot =1.8 #%
    innskud = 10000
    k = 250000
    total = innskud
    aar = 0
    while total < k:
        total = total*(1 + rentefot/100) + innskud
        aar += 1


    print('det tar ', aar, 'aar', total)

def opg2():
    n = 100000
    wins = 0

    for i in range(n):
        t1 = np.random.randint(low=1, high=7)
        t2 = np.random.randint(low=1, high=7)

        if t1>4 or t2>4:
            wins = wins + 1

    print(wins/n)

bread = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275]
expense = [650, 780, 1000, 1150, 1400, 1700, 2000, 2400, 2830, 3300]


def kostnad(x):
    for i in range(len(bread)):
        if x <= bread[i]:
            return expense[i]


def fortjeneste(x):
    return x*27

def overskudd(x):
    return fortjeneste(x) - kostnad(x)

#for n in bread:
#    print(n, kostnad(n)/n, fortjeneste(n), overskudd(n))

Xmaks = 6
j = 18
g = 12

def binom(k, n):
    return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))

def hypergreometrisk(x, j=j,g=g):
    G1 = binom(x, j)
    G2 = binom(Xmaks - x, g)
    G3 = binom(Xmaks, g+j)
    return G1*G2/G3



import matplotlib.pyplot as plt

xs = np.array(range(Xmaks+1))
ys = []
for x in xs:
    ys.append(hypergreometrisk(x))

plt.bar(xs, ys)
plt.show()

print('Sannsynligheten for 1 gutt er:', 1-hypergreometrisk(6))