def gcd(x: int, y: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    """
    if y == 0:
        return x
    else:
        print(y, x%y)
        return gcd(y, x % y)