import math
from sympy import *
import numpy as np

import bisection as bs
import falseposition as fp
import newton as nr


def numberstomethod(n, f, interval, tolerance: float):
    n = int(n)
    x = symbols('x')
    df = f(x).diff(x)
    if n == 1: return bs.bisection(f, interval, tolerance)
    elif n == 2: return fp.falsePosition(f, interval, tolerance)
    elif n == 3: return nr.newtons_method(sympify(f(x)), interval[0], tolerance)             #nr.newton(f, df, interval[0], tolerance)
    else: print("Error Switch")


def main():
    interval = [0 for i in range(2)]
    print('1) Bisection')
    print('2) False position')
    print('3) Newton Raphson')
    n = input('Choose variant: ')
    equation = input("Input function in Py style(power is **, instead of 2x, 2 * x): ")
    f = lambda x: eval(equation.replace('e', 'round(np.exp(1), 7'))
    interval[0] = int(input("interval's first num: "))
    interval[1] = int(input("interval's second num: "))
    tolerance = input("tolerance (1e-5): ")

    numberstomethod(n, f, interval, float(tolerance))


main()
