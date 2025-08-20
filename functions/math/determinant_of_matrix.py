import random

def determinant(matrix: list[list[int]]) -> int:
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    det: int = 0

    for i in range(len(matrix)):
        submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(submatrix)


    return det


matrix = [
  [2, 3, 4],
  [5, 6, 7],
  [8, 9 ,1],
]

print(determinant(matrix))

print("")
