import random

matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def matrixPrint(matrix):
    print("print start-------")
    for row in matrix:
        print(*row)
    print("print end------")


def emptyPlaces(matrix):
    emptyIndex = []
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            if (matrix[row][clm] == 0):
                emptyIndex.append((row, clm))
    return emptyIndex


def returnNum(emptyIndex):
    return emptyIndex[0], emptyIndex[1]


def insertNum(matrix, x, y):
    if (random.random() <= 0.7):
        matrix[x][y] = 2
        return 2
    else:
        matrix[x][y] = 4
        return 4


def checkNull(matrix):
    for row in matrix:
        if 0 in row:
            return True
    return False


def moveLeft(matrix):
    for row in matrix:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if (matrix[i][j] == matrix[i][j + 1]) and (matrix[i][j] != 0):
                matrix[i][j] *= 2
                matrix[i].pop(j + 1)
                matrix[i].append(0)
    matrixPrint(matrix)
    return matrix


def moveRight(matrix):
    for row in matrix:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if matrix[i][j] == matrix[i][j - 1] and matrix[i][j] != 0:
                matrix[i][j] *= 2
                matrix[i].pop(j - 1)
                matrix[i].insert(0, 0)

    matrixPrint(matrix)
    return matrix


def moveUp(matrix):
    for j in range(4):
        column = []
        for i in range(4):
            if matrix[i][j] != 0:
                column.append(matrix[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if (column[i] == column[i + 1]) and (column[i] != 0):
                column[i] *= 2
                column.pop(i + 1)
                column.append(0)
        for i in range(4):
            matrix[i][j] = column[i]
    matrixPrint(matrix)
    return matrix


def moveDown(matrix):
    for j in range(4):
        column = []
        for i in range(4):
            if matrix[i][j] != 0:
                column.append(matrix[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if (column[i] == column[i - 1]) and (column[i] != 0):
                column[i] *= 2
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):
            matrix[i][j] = column[i]
    matrixPrint(matrix)
    return matrix


def Insertion(matrix):
    empty = emptyPlaces(matrix)
    random.shuffle(empty)
    numIndex = empty.pop()
    x, y = returnNum(numIndex)
    value1 = insertNum(matrix, x, y)
    print(f"Element inserted")
    matrixPrint(matrix)
    return value1, x, y


def restart(matrix):
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            matrix[row][clm]=0
    Insertion(matrix)
