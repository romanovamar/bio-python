import numpy as np


def getdimension(n):
    return np.ndim(n)


def getdiagonal(a):
    return a.diagonal()


def cutarray(a, minvalue, maxvalue):
    return a.clip(minvalue, maxvalue, out=a)


def getmoments(a):
    return a.mean(), a.var()


def getdotproduct(a, b):
    return np.dot(a, b)


def checkequal(a, b):
    return np.equal(a, b)


def comparewithnumber(a, bound):
    return np.less(a, bound)


def matrixproduct(a, b):
    return np.matmul(a, b)


def matrixdet(a):
    return np.linalg.det(a)
