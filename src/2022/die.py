import numpy as np

for i in range(10**8):
    sum = 0
    for j in range(6):
        die = np.random.randint(low=1,high=6)
        sum += die
    if sum==6:
        print('WOW')