# takes a funtion from console and range of x values and outputs the function values

import numpy as np
import numpy.linalg as la


def f(x):
    return np.log10(x) ** 2


def main():
    x = np.array([float(x) for x in input("Enter the x values: ").split()])
    y = np.array([f(x) for x in x])
    print(sum(y))


if __name__ == "__main__": main()