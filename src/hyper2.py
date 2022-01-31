import numpy as np
import matplotlib.pyplot as plt
from math import comb

# vi har 10 gutter og 20 jenter i en klasse. Skal trekke 3.
# Hva er sannsynligheten for at 2 av de er gutter
m = 10
n = 60 # gutter + jenter
r = 20

def hypergeometrisk_fordeling(k, m=m, n=n, r=r):
    """
    k er antall gunstige trukket, m er antall gunstige mulige,
    n er antall totalt, og r er antall trukket
    """
    return (comb(m,k)*comb(n-m,r-k))/comb(n,r)

# initialisere listene som lagrer utregningene
probs = []
ks = []

print('k | P(X=k)')
for i in range(r+1):
    print(i,'|', hypergeometrisk_fordeling(i))

    # legger til utregningene våre
    probs.append(hypergeometrisk_fordeling(i))
    ks.append(i)

# plotter alltoid x-akse så y-akse
plt.bar(ks, probs)
plt.title(f'Hypergeometrisk fordeling for n={n}, m={m}, r={r}')
plt.show()