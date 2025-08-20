def multiply(matrix1, matrix2):

    result = []

    for i in range(len(matrix1)):
        res = []
        for j in range(len(matrix2[0])):
            c = 0
            for k in range(len(matrix2)):
                c += matrix1[i][k] * matrix2[k][j]


            res.append(c)

        result.append(res)

    return result
