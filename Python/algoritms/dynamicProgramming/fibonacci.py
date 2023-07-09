import functools
from math import sqrt

def fib_iterative(n:int)->list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using iteration
    >>> fib_iterative(0)
    [0]
    >>> fib_iterative(1)
    [0, 1]
    >>> fib_iterative(5)
    [0, 1, 1, 2, 3, 5]
    >>> fib_iterative(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib_iterative(-1)
    Traceback (most recent call last):
        ...
    Exception: n is negative
    """
      
    if n < 0:
        raise Exception("n is negative")
    if n == 0:
        return [0]
    fib = [0,1]
    for _ in range(n - 1):
        fib.append(fib[-1]+ fib[-2])
    return fib


def fib_recursive(n:int)-> list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using recursion
    >>> fib_iterative(0)
    [0]
    >>> fib_iterative(1)
    [0, 1]
    >>> fib_iterative(5)
    [0, 1, 1, 2, 3, 5]
    >>> fib_iterative(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib_iterative(-1)
    Traceback (most recent call last):
        ...
    Exception: n is negative
    """
    def fib_recursive_term(i:int)->int:
        """
        Calculates the i-th (0-indexed) Fibonacci number using recursion
        """
        if i < 0:
            raise Exception("n is negative")
        if i < 2:
            return i
        return fib_recursive_term(i -1) + fib_recursive_term(i -2)
    if n < 0:
        raise Exception("n is negative")
    return [fib_recursive_term(i) for i in range(n+1)]

def fib_recursive_cached(n:int)->list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using recursion
    >>> fib_iterative(0)
    [0]
    >>> fib_iterative(1)
    [0, 1]
    >>> fib_iterative(5)
    [0, 1, 1, 2, 3, 5]
    >>> fib_iterative(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib_iterative(-1)
    Traceback (most recent call last):
        ...
    Exception: n is negative
    """
    @functools.cache
    def fib_recursive_term(i:int)->int:
        """
        Calculates the i-th (0-indexed) Fibonacci number using recursion
        """
        if i < 0:
            raise Exception("n is negative")
        if i < 2:
            return i
        return fib_recursive_term(i - 1) + fib_recursive_term(i - 2)
    
    if n < 0:
        raise Exception("n is negative")
    return [fib_recursive_term(i) for i in range(n +1)]

def fib_memoization(n:int)-> list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using memoization
    >>> fib_memoization(0)
    [0]
    >>> fib_memoization(1)
    [0, 1]
    >>> fib_memoization(5)
    [0, 1, 1, 2, 3, 5]
    >>> fib_memoization(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib_iterative(-1)
    Traceback (most recent call last):
        ...
    Exception: n is negative
    """   
    if n < 0:
        raise(Exception("n is negative"))
    # Cache must be outside recursuive function
    # other it will reset every time it calls itself.
    cache: dict[int, int] = {0: 0, 1: 1, 2: 1}  # Prefilled cache

    def rec_fn_memoized(num: int)-> int:
        if num in cache:
            return cache[num]
        value = rec_fn_memoized(num - 1) +rec_fn_memoized(num -2)
        cache[num] = value
        return value
    return [rec_fn_memoized(i) for i in range(n + 1)]


def fib_binet(n: int) -> list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using a simplified form
    of Binet's formula:
    https://en.m.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding

    NOTE 1: this function diverges from fib_iterative at around n = 71, likely
    due to compounding floating-point arithmetic errors

    NOTE 2: this function doesn't accept n >= 1475 because it overflows
    thereafter due to the size limitations of Python floats
    >>> fib_binet(0)
    [0]
    >>> fib_binet(1)
    [0, 1]
    >>> fib_binet(5)
    [0, 1, 1, 2, 3, 5]
    >>> fib_binet(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fib_binet(-1)
    Traceback (most recent call last):
        ...
    Exception: n is negative
    >>> fib_binet(1475)
    Traceback (most recent call last):
        ...
    Exception: n is too large
    """
    if n < 0:
        raise Exception("n is negative")
    if n >= 1475:
        raise Exception("n is too large")
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5) / 2
    return [round(phi**i / sqrt_5) for i in range(n + 1)]



print(fib_binet(5))