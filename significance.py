import math
def factorialLimited(n, lowerlimit):
    total = n
    n -= 1

    while n > lowerlimit:
        total *= n
        n -= 1
    return total

def combinations( n, k ):
    #optimized to only compute the smaller factorial
    # n!/(k!(n-k)!) -> n!/(k!c!)

    if n == k or k == 0:
        return 1

    c = n - k

    if k > c:
        return factorialLimited(n, k)/math.factorial(c)
    else:
        return factorialLimited(n, c)/math.factorial(k)


def significance( p, n, k ):
    print(p)
    print(n)
    print(k)
    return combinations(n,k) * (p ** k) * ((1 - p)**(n-k))
