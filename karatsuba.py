def karatsuba(x,y):
    if (len(str(x)) == 1 or len(str(x)) == 1):
        return x*y
    n = max(len(str(x)), len(str(y)))
    mid = int(n // 2)
    x1 = int(x // 10**(mid))
    x0 = int(x % 10**(mid))
    y1 = int(y // 10**(mid))
    y0 = int(y % 10**(mid))
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba((x0 + x1), (y0 + y1)) - z0 - z2
    z = z2 * 10**n + z1*10**mid + z0
    return z
