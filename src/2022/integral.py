# parametere
n = 4
start = 1
slutt = 5
f = lambda x: x**2 + 1


# finner integralet
a = 0
dx = (slutt - start)/n

for i in range(n):
    a += f(start + i*dx)*dx

print(a)