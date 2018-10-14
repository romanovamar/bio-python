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


def combinationswithrepeats(n, k):
    p=1
    def gen_comb(n, k, p, prefix=[]):
        if len(prefix) == k:
            yield tuple(prefix)
        for i in range(p, n + 1):
            if len(prefix) <= k:
                yield from gen_comb(n, k, p, prefix + [i])
            p += 1

    return list(gen_comb(n, k, p))


def unorderedpartitions(n):
    f=1
    def gen(n, f, prefix=[]):
        if sum(prefix) == n:
            yield tuple(prefix)
        for i in range(f, n + 1):
            if len(prefix) <= n:
                yield from gen(n, f, prefix + [i])
            f += 1

    return list(gen(n, f))


