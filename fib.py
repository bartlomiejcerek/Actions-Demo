from typing import Optional


def fib(n: int) -> int:
    """
    Simple function that return nth Fibonacci number

    Args:
        n (int): Positive integer for which you want to get Fibonacci number

    Returns:
        int: nth Fibonacci number

    Raises:
        Value Error if n is not an imteger or is negative

    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("n must be positive integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_cache(n: int, cache: Optional[dict[int, int]] = None) -> int:
    """
    Cached function that returns nth Fibonacci number

    Args:
        n (int): Positive integer for which you want to get Fibonacci number

    Returns:
        int: nth Fibonacci number

    Raises:
        Value Error if n is not an imteger or is negative

    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("n must be positive integer")

    if cache is None:
        cache = {0: 0, 1: 1}

    if n not in cache:
        cache[n] = fib_cache(n - 1, cache=cache) + fib_cache(n - 2, cache=cache)

    return cache[n]
