import Jacobi as jacobi


def main():
    n = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input("Enter the " + str(i + 1) + " " + str(j + 1) + " element: ")))
        matrix.append(row)

    print(matrix)
    b = []
    for i in range(n):
        b.append(int(input("Enter the " + str(i + 1) + " element of b: ")))
    x = []
    for i in range(n):
        x.append(int(input("Enter the " + str(i + 1) + " element of initial guess: ")))
    iter_num = int(input("Enter the number of iterations: "))
    ans = jacobi.Jacobi(matrix, b, x, iter_num)
    print("The solution is: ", ans)


if __name__ == "__main__":
    main()