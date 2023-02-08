# find determinant of a matrix

import numpy as np
import numpy.linalg as la


def determinant(A):
    return la.det(A)

def main():
    n = int(input("Enter the order of the matrix: "))
    A = np.zeros((n,n), float)
    print("Enter the matrix row by row:")
    for i in range(n):
        A[i] = [float(x) for x in input().split()]
    print("The determinant is: ", determinant(A))

if __name__ == "__main__": main()