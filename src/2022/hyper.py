import numpy as np
import matplotlib.pyplot as plt
from math import comb


def hypergeometrisk_fordeling(k, m, n, r):
    """
    k er antall gunstige trukket, m er antall gunstige mulige,
    n er antall totalt, og r er antall trukket
    """
    return (comb(m,k)*comb(n-m,r-k))/comb(n,r)

# vi har 10 gutter og 20 jenter i en klasse. Skal trekke 3.
# Hva er sannsynligheten for at 2 av de er gutter
m = 10
n = 10 + 20 # gutter + jenter
r = 3
k = 3

print(hypergeometrisk_fordeling(k, m, n, r))