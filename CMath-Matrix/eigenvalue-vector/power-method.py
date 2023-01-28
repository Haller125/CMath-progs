# finds eigenvalue and eigenvector of a matrix using power method and outputs every iteration to console

import numpy as np
import numpy.linalg as la

def powerMethod(A, tol=1.0e-3):
    n = len(A)
    x = np.zeros(n, float)
    x[0] = 1.0
    yprev = np.zeros(n, float)
    for k in range(100):
        y = A*x
        y = [sum(y[i]) for i in range(n)]
        x = y/la.norm(y, np.inf)
        err = la.norm(A*x - x*la.norm(A, np.inf), np.inf)
        print("Iteration", k, "x =", x, "lambda =", la.norm(A, np.inf))
        if (err < tol) or abs(np.subtract(y, yprev)).all() < tol:
            return x, la.norm(A, np.inf)
        yprev = y
    print("powerMethod did not converge")

def main():
    n = int(input("Enter the order of the matrix: "))
    A = np.zeros((n,n), float)
    print("Enter the matrix row by row:")
    for i in range(n):
        A[i] = [float(x) for x in input().split()]
    x, lam = powerMethod(A)
    print("The eigenvalue is", lam)
    print("The eigenvector is", x)

if __name__ == "__main__": main()