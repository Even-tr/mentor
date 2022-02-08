
import math as m

def binom_cof(n, k):
    #Beregner binomialkoefisienten: 'n velger k'
    return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))

n = 3
p = 0.514
k = 2

def binom_dist(k, p=p, n=n):
    # Beregner punktsannsynligheten til binomialfordelingen,
    # altså sannsynligheten for å få k suksesser gitt n uavhengige
    # forsøk, med sannsynliget p.

    # k: antall sksesser
    # p: sannsynlighet for suksess
    # n: antall forsøk

    return binom_cof(n,k)*p**k*(1-p)**(n-k)

def negativ_binom(n, p=p, k=k):
    # Beregner punnktsannsynligheten til den negative binomiske fordelingen.
    # Den beregner sannsynligheten for å trenge n forsøk gitt k suksesser totalt.
    assert n >= k, 'number of trials must be larger or equal to number of successes'
    return binom_cof(n-1, k-1)*p**k*(1-p)**(n-k)

print(binom_dist(2))

print(f'Binomsik fordeling med parameter: n={n}, p={p}')
print(' k  | p(X=k)')
for i in range(n+1):
    print(f'{i: 2}  | {binom_dist(i)}')

print(f'Binomsik fordeling med parameter: k={k}, p={p}')

print(' n  | p(X=n)')
for i in range(k, 10):
    print(f'{i: 2}  | {negativ_binom(i)}')
