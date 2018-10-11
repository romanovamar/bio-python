'''def factorial(n):
Calculate factorial of n. n >= 0'''


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def digitsum(n):
    if n < 10:
        return n
    return n % 10 + digitsum(n // 10)


def reversestring(s):
    if len(s) <= 1:
        return s
    return s[-1] + reversestring(s[:-1])


def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0 and m > 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))
