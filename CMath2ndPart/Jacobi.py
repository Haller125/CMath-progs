import numpy as np


def Jacobi(Matrix, b, x=None, iter_num=25):
    if x is None:
        x = np.zeros(len(Matrix[0]))

    Diag = np.diag(Matrix)
    Diagfulled = Matrix - np.diagflat(Diag)

    for i in range(iter_num):
        x = (b - np.dot(Diagfulled, x)) / Diag
        print('Iteration {}: {}'.format(i, x))
    return x

# Compare this snippet from Gauss-Seidal.py:

# import numpy as np

# def Gauss_Seidal(Matrix, b, x=None, iter_num=25):

