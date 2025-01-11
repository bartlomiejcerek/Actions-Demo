import logging
import os
import time
from typing import Callable

import pytest

from fib import fib, fib_cache

print("Current working directory:", os.getcwd())

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.mark.parametrize(
    "fib_function, n, expected",
    [
        (fib, 0, 0),  # Test base case for normal (Fibonacci
        (fib, 1, 1),  # Test base case for normal Fibonacci
        (fib, 10, 55),  # Test medium Fibonacci number
        (fib_cache, 0, 0),  # Test base case for cached Fibonacci
        (fib_cache, 1, 1),  # Test base case for cached Fibonacci
        (fib_cache, 10, 55),  # Test medium Fibonacci number
    ],
)
def test_fib_functions(fib_function: Callable, n: int, expected: int) -> None:
    """Test both cached and normal Fibonacci functions."""
    assert fib_function(n) == expected
