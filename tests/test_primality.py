import pytest

from superfib.superfib import fibonacci
from superfib.primality import is_prime, known_fib_primes


@pytest.mark.parametrize('n', known_fib_primes)
def test_known_fib_primes(n):
    assert is_prime(n)


def test_no_false_negs_in_500():
    for n in fibonacci(500):
        if is_prime(n):
            assert n in known_fib_primes
