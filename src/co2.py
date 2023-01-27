from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# Leser filen og henter ut kolonnene av interesse manuelt
with open ('data/co2_mm.txt') as file:
    aar = []
    co2 = []
    for line in file.readlines():
        tmp = [float(i) for i in line.split()]
        aar.append(tmp[2])
        co2.append(tmp[3])

# Endrer datastrukturen til numpy array, som er raskere
n = len(aar)
x = np.array(aar)
y = np.array(co2)


# Definerer modellen vår som vi skal prøve å tilpasse dataen
def func(t, a,b,c,d, e):
    return a*np.exp(b*t) + c*np.sin(2+np.pi*t + d)**2 + e

# Dataen burde ikke ha så ekstreme verdier, da kan estimeringen villedes.
# Derfor er det lurt å sentrere tidspunktene rundt år null
offset = 2015

# Finner parameterene
[a,b,c,d, e] = curve_fit(func, x - offset, y)[0]

# Lager x-verdier til å plotte kruver
t= np.linspace(x[0], x[-1], 5000) - offset

# Avlsutter med å plotte resultatene
plt.plot(x, y, '.', label='Observasjoner')
plt.plot(t+offset, func(t,a,b,c,d,e), label='tilpasset kurve')
plt.plot(t+offset, func(t,a,b,0,d,e+c/2), label='tilpasset kurve uten svingninger')
plt.legend()

plt.show()
