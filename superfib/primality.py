def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    # n is definitely composite
    return True


def is_prime(n, _precision_for_huge_n=16):
    """Miller-Rabin primality test
    https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    """
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    ranges = [
        (1373653, (2, 3)),
        (25326001, (2, 3, 5)),
        (118670087467, (2, 3, 5, 7)),
        (2152302898747, (2, 3, 5, 7, 11)),
        (3474749660383, (2, 3, 5, 7, 11, 13)),
        (341550071728321, (2, 3, 5, 7, 11, 13, 17)),
    ]
    # special case
    if n == 3215031751:
        return False

    for upper, bases in ranges:
        if n < upper:
            return not any(_try_composite(a, d, n, s) for a in bases)

    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

# All the primes within the first 500 fibonacci numbers
# from http://oeis.org/A005478
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable301.html
known_fib_primes = [2,3,5,13,89,233,1597,28657,514229,433494437,
 2971215073,99194853094755497, 1066340417491710595814572169,
 19134702400093278081449423917,
 475420437734698220747368027166749382927701417016557193662268716376935476241,
529892711006095621792039556787784670197112759029534506620905162834769955134424689676262369,
1387277127804783827114186103186246392258450358171783690079918032136025225954602593712568353,
3061719992484545030554313848083717208111285432353738497131674799321571238149015933442805665949,
]
