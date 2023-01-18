def x(x, y, z):
    return 27 * x + 6 * y - z

def y(x, y, z):
    return x + y + 54 * z

def z(x, y, z):
    return 6*x + 15 * y + 2 * z

def main():
    x1 = float(input("Enter the value of x: "))
    y1 = float(input("Enter the value of y: "))
    z1 = float(input("Enter the value of z: "))

    print("The value of x is: ", x(x1, y1, z1))
    print("The value of y is: ", y(x1, y1, z1))
    print("The value of z is: ", z(x1, y1, z1))


if __name__ == "__main__":
    main()