import numpy as np
import math


def outIter(i, num):
    print('Iteration N', i, 'x = ', num)


def validate_interval(f, x0, x1):
    return f(x0) * f(x1) < 0


def error_bound(a, b, err):
    n = np.log((b - a) / err) / np.log(2)
    return int(np.ceil(n))


def tolNf(tol):
    return int(str(tol)[-1:]) if int(str(tol)[-1:]) > 4 else len(str(tol)) - 2


def bisection(f, interval, tol=1e-5):
    l = len(str(tol))
    tolN = tolNf(tol)
    x0, x1 = interval[0], interval[1]
    print('interval:', x0, x1)
    counter = 1
    while True:
        root_approx = x0 + ((x1 - x0) / 2)
        y = f(root_approx)
        if -tol < y < tol or counter > 100:
            return outIter(counter, round(root_approx, tolN))
        if round(f(x0) * f(round(root_approx, tolN + 2)), tolN + 2) < 0:
            x1 = round(root_approx, tolN * 2)
            outIter(counter, round(root_approx, tolN))
        else:
            x0 = round(root_approx, tolN * 2)
            outIter(counter, round(root_approx, tolN))
        counter += 1
