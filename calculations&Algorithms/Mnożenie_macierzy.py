import numpy as np


def main():
    matrix1 = np.random.random((2, 2))
    matrix2 = np.random.random((2, 2))

    product = np.zeros((len(matrix1), len(matrix1[0])))

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            for k in range(len(matrix2)):
                product[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Matrix1 = \n", matrix1)
    print("Matrix2 = \n", matrix2)
    print("Product of matrices = \n", product)


if __name__ == "__main__":
    main()