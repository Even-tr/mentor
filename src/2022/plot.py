from pylab import *

rom = ['a','b','c']
p = [100, 2, 30]
p = array(p)
p = p/p.sum()
print(p)

lykkehjul = choice(rom,p=p)
print(lykkehjul)