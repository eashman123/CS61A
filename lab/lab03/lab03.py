def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b==0:
        return 0 + c
    elif a==0:
        return 0 + c
    elif b==1:
        return a+c
    else:
        return a + ab_plus_c(a, b-1, c)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    >>> gcd(5, 10)
    5
    """
    temp =  max(a, b)
    a = min(a, b)
    b = temp
    if b%a==0:
        return a
    else:
        return gcd(a, b%a)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    if n != 1:
        if n%2 == 0:
            a = hailstone(int(n/2))
            return a + 1
        else:
            a = hailstone(int(3*n+1))
            return a + 1
    return 1
