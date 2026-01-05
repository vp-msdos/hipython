"""
functiona call itslef
"""

def fact(n):
    """
    On a given number it calculates the factorial of it.
    :param n:
    :return: int
    """
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(4))