import bisection as bs


def falsePosition(f, interval, tol=1e-5):
    x0, x1 = interval[0], interval[1]
    counter = 1
    condition = True
    print('interval:', x0, x1)
    while condition:
        tolN = bs.tolNf(tol)
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        bs.outIter(counter,  round(x2, tolN))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        counter = counter + 1
        condition = abs(f(x2)) > tol