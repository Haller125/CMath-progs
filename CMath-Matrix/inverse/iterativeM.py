# matrix inverse by iterative method

import numpy as np
import numpy.linalg as la


def iterativeM(A, tol=1.0e-9):
    n = len(A)
    I = np.eye(n)
    X = I
    for k in range(100):
        X = 0.5*(X + la.inv(A)*X)
        err = la.norm(A*X - I, np.inf)
        if err < tol: return X
    print("iterativeM did not converge")


# takes matrix from console
def main():
    n = int(input("Enter the order of the matrix: "))
    A = np.zeros((n,n), float)
    print("Enter the matrix row by row:")
    for i in range(n):
        A[i] = [float(x) for x in input().split()]
    X = iterativeM(A)

    print("The inverse is:")

    for i in range(n):
        for j in range(n):
            print("%12.6f" % X[i,j], end='')
        print()


if __name__ == "__main__": main()
