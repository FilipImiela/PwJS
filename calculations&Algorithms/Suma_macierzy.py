import numpy as np


def main():

    matrix1 = np.random.random((128, 128))
    matrix2 = np.random.random((128, 128))

    su = np.zeros((len(matrix1), len(matrix1[0])))

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            su[i][j] = matrix1[i][j] + matrix2[i][j]

    print("Matrix1 = \n", matrix1)
    print("Matrix2 = \n", matrix2)
    print("Product of matrices = \n", su)


if __name__ == "__main__":
    main()




