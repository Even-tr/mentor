

def f(x):
    return 2*x + 1

x1, x2 = 0, 1
assert x1<x2

for n in [1,2,3,4,6,8,10,20,100,1000]:
    d = (x2-x1)/n
    upper = 0
    for i in range(n):
        f1 = f(x1 + i*d)
        f2 = f(x1 + i*d+d)
        upper += max(f1, f2)*d

    lower = 0
    for i in range(n):
        f1 = f(x1 + i*d)
        f2 = f(x1 + i*d+d)
        lower += min(f1, f2)*d

    print(n, lower, upper)