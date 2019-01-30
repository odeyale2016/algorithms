# Uses python3

from sys import stdin
import random

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fib_seq(limit=None):
    a = 0
    yield a
    b = 1
    yield b
    if limit is None:
        while True:
            a, b = b, a + b
            yield b
    else:
        for _ in range(limit):
            a, b = b, a + b
            yield b


def fib(n, mod=1):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b % mod, a + b
    return a % mod


def pisano(mod):
    if mod == 1:
        return 1
    fib_mod = (fib % mod for fib in fib_seq())
    _ = next(fib_mod)
    prev = next(fib_mod)
    fib = next(fib_mod)
    for period, fib in enumerate(fib_mod, 2):
        if prev == 0 and fib == 1:
            return period
        else:
            prev = fib


def fibonacci_sum_squares_optimized(pos_to):
    if pos_to <= 1:
        return pos_to

    total = 0

    period = pisano(10)
    fib_mod_sqr = [(fib ** 2) % 10 for fib in fib_seq(period - 2)]

    total  = sum(fib_mod_sqr) * (pos_to // 10)
    total += sum(fib_mod_sqr[:pos_to % period + 1])

    return total % 10


def stress():
    random.seed(0)
    while True:
        pos_to = random.randrange(1, 200)
        naive = fibonacci_sum_squares_naive(pos_to)
        optimized = fibonacci_sum_squares_optimized(pos_to)
        if naive == optimized:
            print("%20s: %s" % ("{pos_to}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for {pos_to}: ".format(
                **locals()) + "{naive} != {optimized}".format(**locals()))




if __name__ == '__main__':
#     stress()
    n = int(stdin.read())
    print(fibonacci_sum_squares_optimized(n))
