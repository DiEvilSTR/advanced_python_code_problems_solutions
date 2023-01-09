from collections import Counter

# I googled it
# The answer is get by using Burnsides lemma

def gcd(i, j):
    while j:
        i, j = j, i % j
    return i


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def cycle_count(c, n):
    cc = factorial(n)
    for a, b in Counter(c).items():
        cc //= (a ** b) * factorial(b)
    return cc


def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n // 2 + 1):
        for p in cycle_partitions(n-i, i):
            yield [i] + p


def solution(w, h, s):
    grid = 0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            m = cycle_count(cpw, w) * cycle_count(cph, h)
            grid += m * (s ** sum([sum([gcd(i, j) for i in cpw]) for j in cph]))

    return str(grid // (factorial(w)*factorial(h)))


solution(2, 2, 2)
solution(2, 3, 4)