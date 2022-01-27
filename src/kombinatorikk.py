"""
Vi har en kurv med 5 kuler, 3 røde og 2 blå.
Vi skal simulere svarene
"""

import numpy as np
import pylab 

N = 10000 # antal ganger vi simulerer
kuler = np.array([1, 1, 1, 0, 0]) # B=0, R=1

#P(BR)?
counter = 0
for i in range(N):
    trekk = pylab.choice(kuler, size=2 ,replace=False)
    #print(trekk)

    # Her finner vi de 'gunstige' utfallene
    if trekk[0]==0 and trekk[1] == 1:
        counter = counter + 1

print('P(BR) =',counter/N)
"""
P(BR) = P(B)*P(R|B) = (2/5) * (3/4) = 6/20 = 3/10
"""

#P(XR)?
counter = 0
for i in range(N):
    trekk = pylab.choice(kuler, size=2 ,replace=False)
    #print(trekk)

    # Her finner vi de 'gunstige' utfallene
    if trekk[1] == 1:
        counter = counter + 1

print('P(XR) =',counter/N)
"""
P(XR) = P(BR) + P(RR) = 3/10 + (3/5) * (2/4) 
    = 3/10 + 6/20 = 3/10 + 3/10 = 6/10
"""
