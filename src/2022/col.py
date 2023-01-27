from math import sqrt

# konstanter
c = 3*10**8
m_p = 1.67*10**(-27)

# parametere
v_p = 1.8*10**8


def gamma(v):
    return 1/sqrt(1-v**2/c**2)

def kinetic(m, v):
    return (gamma(v) -1)*m*c**2

ek = kinetic(m_p, v_p)
print(f'kinetic energy {ek} J')