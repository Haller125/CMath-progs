# finds forward difference table of a function

import numpy as np
import numpy.linalg as la


def forwardDifferenceTable(x, y):
    n = len(x)
    F = np.zeros((n,n), float)
    F[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            F[i,j] = F[i+1,j-1] - F[i,j-1]
    return F


def main():
    x = np.array([float(x) for x in input("Enter the x values: ").split()])
    y = np.array([float(x) for x in input("Enter the y values: ").split()])
    F = forwardDifferenceTable(x, y)
    n = len(x)
    print("The forward difference table is:")
    for i in range(n):
        for j in range(n-i):
            print("%12.3f" % F[i,j], end='')
        print()


if __name__ == "__main__": main()