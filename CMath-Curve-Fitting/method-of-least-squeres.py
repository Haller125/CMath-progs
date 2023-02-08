# finds function that fits data using method of least squares

import numpy as np
import numpy.linalg as la

def leastSquares(x, y, n):
    m = len(x)
    A = np.zeros((m,n+1))
    for i in range(m):
        for j in range(n+1):
            A[i,j] = x[i]**j
    c = la.solve(A.T@A, A.T@y)
    return c

def main():
    n = int(input("Enter the order of the polynomial: "))
    x = np.array([float(x) for x in input("Enter the x values: ").split()])
    y = np.array([float(x) for x in input("Enter the y values: ").split()])
    c = leastSquares(x, y, n)
    print("The coefficients are:")
    for i in range(n+1):
        print("%12.6f" % c[i])

if __name__ == "__main__": main()