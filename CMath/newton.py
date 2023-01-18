import math
import numpy as np
from sympy import *

import bisection as bs

x = symbols('x')


def newtons_method(f, x0, tol=1e-12, start = 0):
    n = 1

    tolN = bs.tolNf(tol)
    dy = diff(f)
    x_n = x - (f / dy)
    root_approx = x0
    y_n = f.subs(x, x0)
    dy_n = dy.subs(x, x0)
    if not start:
        print("Start value:", x0)
        start = True
    while not -tol < y_n.evalf() < tol:
        root_approx = x_n.subs([(x, root_approx), (f, y_n), (dy, dy_n)])
        root_approx = round(root_approx, tolN*2)
        bs.outIter(n, round(root_approx, tolN))
        y_n = f.subs(x, round(root_approx, tolN * 2))
        dy_n = dy.subs(x, round(root_approx, tolN * 2))
        n += 1
    return bs.outIter(n, round(root_approx, tolN))
