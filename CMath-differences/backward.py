# outputs backward differences table to console

import numpy as np
import numpy.linalg as la


def backwardDifferenceTable(x, y):
    n = len(x)
    F = np.zeros((n,n), float)
    F[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            F[i,j] = F[i,j-1] - F[i+1,j-1]
    return F


def main():
    x = np.array([float(x) for x in input("Enter the x values: ").split()])
    y = np.array([float(x) for x in input("Enter the y values: ").split()])
    F = backwardDifferenceTable(x, y)
    n = len(x)
    print("The backward difference table is:")
    for i in range(n):
        for j in range(n-i):
            print("%12.3f" % F[i,j], end='')
        print()