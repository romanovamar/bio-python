def permutations(n):
    def generator(n, prefix=[]):
        if len(prefix) == n:
            yield tuple(prefix)
        for i in range(1, n + 1):
            if i not in prefix:
                yield from generator(n, prefix + [i])

    return list(generator(n))


def correctbracketsequences(n):
    def gen(s, debt):
        variants = []
        if len(s) == n * 2:
            variants.append(s)
        else:
            if debt == 0:
                variants.extend(gen(s + '(', debt + 1))
            elif debt > 0 and n * 2 - len(s) > debt:
                variants.extend(gen(s + '(', debt + 1))
                variants.extend(gen(s + ')', debt - 1))
            elif n * 2 - len(s) == debt:
                variants.extend(gen(s + ')', debt - 1))
        return variants

    return gen('(', 1)


print(correctbracketsequences(3))


def correct(n):
    def gen(i, j):
        brackets = ['(']
        if len(i) == 2 * n:
            return brackets
        for f in ['(', ')']:
            if
