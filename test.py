def valuesunion(*dicts):
    result = set()
    for dict in dicts:
        for i in dict.values():
            result.add(i)
    return result


def powers(n, m):
    d = {i: i ** i % m for i in range(1, n + 1)}
    return d


from functools import reduce

fibonacci = lambda n: reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


def popcount(n):
    t = 0
    x = '' if n > 0 else "0"
    while n > 0:
        y = str(n % 2)
        x = y + x
        n = int(n // 2)
    for i in x:
        if i == '1':
            t += 1
    return t


def popcount(n):
    return bin(n).count('1')


def isIPv4(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


import itertools


def pascals():
    s = (1,)

    for i in itertools.count(1):
        line = []
        line.append(1)
        for i in range(len(s) - 1):
            line.append(s[i] + s[i + 1])
        line.append(1)
        yield tuple(s)
        s = line
