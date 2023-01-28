# finds inverse of a matrix using Cayley-Hamilton theorem

import numpy as np
import numpy.linalg as la


def inverse(A, tol=1.0e-9):
    n = len(A)
    I = np.eye(n)
    X = I
    for k in range(100):
        X = 0.5*(X + la.inv(A)*X)
        err = la.norm(A*X - I, np.inf)
        if err < tol: return X
    print("iterativeM did not converge")