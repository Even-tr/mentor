import imp
from pylab import *
import matplotlib.pyplot as plt

trials = []
upper= []
lower= []
for trial in range(10):
    N = 100
    terningkast = []
    for i in range(N):
        terningkast.append(randint(1,7))

    terningkast = array(terningkast)
    n = sum(terningkast == 6)
    r = n/N
    trials.append(r)
    print('simulert: ', r)
    feilmaring = 2*sqrt(r*(1-r)/N)
    upper.append(r+feilmaring)
    lower.append(r-feilmaring)
print('faktisk: ', 1/6)
print(trials)

print(array(upper).mean())
print(array(lower).mean())