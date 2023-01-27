
f1 = 1
f2 = 1

for i in range(100):
    print(f1, f2/f1)
    temp = f1 + f2
    f1 = f2
    f2 = temp


def Fibonacci(n):
    # NB: En veldig dårlig algoritme
    # Base case
    if n == 1 or n == 2:
        return 1
    
    return Fibonacci(n-1) + Fibonacci(n-2)

