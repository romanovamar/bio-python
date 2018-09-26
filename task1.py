def unique(e):
    return sorted(set(e))


def transposeDict(d):
    s = []
    for i in d.values():
        assert i not in s, 'Values must be different'
        s.append(i)
    return {d[key]: key for key in d}


def mex(e, i=1):
    assert type(e) == list, 'Wrong type'
    return i if i not in e else mex(e, i=i + 1)


def frequencyDict(s):
    assert type(s) != str, 'Wrong type'
    return {i: s.count(i) for i in s}


if __name__ == "__main__":
    assert unique([1, 2, 1, 3]) == [1, 2, 3]
    assert unique({5, 1, 3}) == [1, 3, 5]
    assert unique('adsfasdf') == ['a', 'd', 'f', 's']

    assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}
    assert transposeDict({1: 1}) == {1: 1}
    assert transposeDict({}) == {}

    assert mex([1, 2, 3]) == 4
    assert mex(['asdf', 123]) == 1
    assert mex([0, 0, 1, 0]) == 2

    assert frequencyDict('') == {}
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1}
