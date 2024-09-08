from decimal import Decimal


def nsqrt(x, p):
    x0 = x
    f = lambda y: y**p - x0
    df = lambda y: p * y ** (p - 1)
    for n in range(1000):
        x1 = x - f(x) / df(x)
        #if abs(x1 - x) <= 10**(-40):
        #    break
        x = x1
    return x1

eps = Decimal('1.0')
while 1 + eps / 2 != 1:
    eps /= 2


