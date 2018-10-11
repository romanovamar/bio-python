from functools import reduce


def squares(a):
    for i in a:
        yield i ** 2


def repeatntimes(elems, n):
    for i in range(n):
        for f in elems:
            yield f
            
def repeatntimes(elems, n):
    l = []
    for i in elems:
        l.append(i)
        yield i
    yield from l * (n - 1)


def evens(x):
    even = x if x % 2 == 0 else x + 1
    while True:
        yield even
        even += 2


def digitsumdiv(p):
    f = p
    while True:
        if sum([int(i) for i in str(p)]) % f == 0:
            yield int(p)
        p += 1


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.lower() if x.isupper() else x.upper(), s)


def productif(elems, conds):
    conds = iter(conds)
    return reduce(lambda x, y: x * y, filter(lambda f: next(conds), elems), 1)
