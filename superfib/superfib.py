from .primality import is_prime


def fibonacci(n):
    """generates the first n fibonacci numbers
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def superfib(n):
    """generates the first n fibonacci numbers while printing:
        * "Buzz" when F(n) is divisible by 3.
        * "Fizz" when F(n) is divisible by 5.
        * "FizzBuzz" when F(n) is divisible by 15.
        * "BuzzFizz" when F(n) is prime.
        * the value F(n) otherwise.
    """
    for i in fibonacci(n):
        fizz = 'Fizz' if i % 3 == 0 else ''
        buzz = 'Buzz' if i % 5 == 0 else ''
        if fizz or buzz:
            print(fizz+buzz)
            continue

        if is_prime(i):
            print('BuzzFizz')
        else:
            print(i)
