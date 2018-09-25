def listToString(a):
    return '[{}]'.format(', '.join([str(i) for i in a]))


def addBorder(a):
    c = ['+{}+'.format('-' * len(a[0]))]
    for i in a:
        c.append('|{}|'.format(i))
    c.append(c[0])
    return c


def shorting(e):
    c = []
    for i in e:
        if len(i) <= 10:
            c.append(i)
        else:
            t = '{}{}{}'.format(i[0], len(i[1:-1]), i[-1])
            c.append(t)
    return c


def competition(e, k):
    c = []
    for i in e:
        if i >= e[k] and i != 0:
            c.append(i)
    return len(c)


def goodPairs(a, b):
    c = []
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                c.append(i ** 2 + j ** 2)
    return sorted(set(c))


def makeShell(n):
    f = 0
    a = []
    for i in range(2 * n - 1):
        if i < n:
            f += 1
            a.append(f * [0])
        if i >= n:
            f -= 1
            a.append(f * [0])
    return a
