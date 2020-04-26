import pygame
from pygame.locals import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open
import keyboard
import sys
import random

edges=()  #НЕ ЗАБУТИ!!: ЗЛІВА ВЕРХ НА ПРАВО(ПРОТИ ГОДИН)

matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 2, 0, 0]
]

textureCoords = (
    (0.0, 1.0),
     (0.0, 0.0),
     (1.0, 0.0),
     (1.0, 1.0)
)

verticies = (

    # 1
    ((-0.6, 0.6),
     (-0.6, 0.32),
     (-0.34, 0.32),
     (-0.34, 0.6)),
    # 2
    ((-0.28, 0.6),
     (-0.28, 0.32),
     (-0.02, 0.32),
     (-0.02, 0.6)),
    # 3
    ((0.04, 0.6),
     (0.04, 0.32),
     (0.3, 0.32),
     (0.3, 0.6)),
    # 4
    ((0.36, 0.6),
     (0.36, 0.32),
     (0.64, 0.32),
     (0.64, 0.6)),
    # 5
    ((-0.6, 0.26),
     (-0.6, -0.02),
     (-0.34, -0.02),
     (-0.34, 0.26)),
    # 6
    ((-0.28, 0.26),
     (-0.28, -0.02),
     (-0.02, -0.02),
     (-0.02, 0.26)),
    # 7
    ((0.04, 0.26),
     (0.04, -0.02),
     (0.3, -0.02),
     (0.3, 0.26)),
    # 8
    ((0.36, 0.26),
     (0.36, -0.02),
     (0.64, -0.02),
     (0.64, 0.26)),
    # 9
    ((-0.6, -0.08),
     (-0.6, -0.36),
     (-0.34, -0.36),
     (-0.34, -0.08)),
    # 10
    ((-0.28, -0.08),
     (-0.28, -0.36),
     (-0.02, -0.36),
     (-0.02, -0.08)),
    # 11
    ((0.04, -0.08),
     (0.04, -0.36),
     (0.3, -0.36),
     (0.3, -0.08)),
    # 12
    ((0.36, -0.08),
     (0.36, -0.36),
     (0.64, -0.36),
     (0.64, -0.08)),
    # 13
    ((-0.6, -0.42),
     (-0.6, -0.7),
     (-0.34, -0.7),
     (-0.34, -0.42)),
    # 14
    ((-0.28, -0.42),
     (-0.28, -0.7),
     (-0.02, -0.7),
     (-0.02, -0.42)),
    # 15
    ((0.04, -0.42),
     (0.04, -0.7),
     (0.3, -0.7),
     (0.3, -0.42)),
    # 16
    ((0.36, -0.42),
     (0.36, -0.7),
     (0.64, -0.7),
     (0.64, -0.42))

)

texture0 = pygame.image.load('0.png')
texture2 = pygame.image.load('2.png')
texture4 = pygame.image.load('4.png')
texture8 = pygame.image.load('8.png')
texture16 = pygame.image.load('16.png')
texture32 = pygame.image.load('32.png')
texture64 = pygame.image.load('64.png')

textures = {
    0: texture0,
    2: texture2,
    4: texture4,
    8: texture8,
    16: texture16,
    32: texture32,
    64: texture64
}

def matrixPrint(matr):
    print("print start-------")
    for row in matr:
        print(*row)
    print("print end------")

def emptyPlaces(matr):
    emptyIndex=[]
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            if(matr[row][clm]==0):
                emptyIndex.append((row,clm))
    return emptyIndex


def returnNum(emptyIndex):
    return emptyIndex[0],emptyIndex[1]


def insertNum(matrix,x,y):
    if(random.random()<=0.7):
        matrix[x][y]=2
        return 2
    else:
        matrix[x][y]=4
        return 4


def checkNull(matrix):
    for row in matrix:
        if 0 in row:
            return True
    return False

def swapTexture(matrix):
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            value=matrix[row][clm]
            verticiesId=row*4+clm
            subTex(textures[value],verticiesId)





matrixPrint(matrix)

def moveLeft(matrix):
    for row in matrix:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if (matrix[i][j]==matrix[i][j+1]) and (matrix[i][j]!=0):
                matrix[i][j]*=2
                matrix[i].pop(j+1)
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
                column.insert(0,0)
        for i in range(3,0,-1):
            if (column[i] == column[i - 1]) and (column[i] != 0):
                column[i] *= 2
                column.pop(i - 1)
                column.insert(0,0)
        for i in range(4):
            matrix[i][j] = column[i]
    matrixPrint(matrix)
    return matrix

def subTex(textureSurface,verticiesId):

    TextureData = pygame.image.tostring(textureSurface, "RGBA",1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    texid = glGenTextures(1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, TextureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glBegin(GL_QUADS)
    for j in range(4):
      glTexCoord2f(textureCoords[j][0], textureCoords[j][1])
      glVertex2f(verticies[verticiesId][j][0],verticies[verticiesId][j][1])

    glEnd()
    glFlush()
    return texid

def Cube():
     glBegin(GL_QUADS)
     for vertex in verticies:
          for elem in vertex:
             glVertex2f(elem[0],elem[1])
     glEnd()
     glFlush()

def keybrd(key,x,y):
    ch=ord(key.decode("ascii"))
    if ch==13:
        swapTexture(matrix)
        print("start")

    if(chr(ch)=='q'):
        sys.exit("exit")

    if(chr(ch)=='a'):
        print("event left")
        moveLeft(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
        else:
            sys.exit("Player lost")
        swapTexture(matrix)

    if(chr(ch)=='s'):
        print("event down")
        moveDown(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
        else:
            sys.exit("Player lost")
        swapTexture(matrix)

    if(chr(ch)=='w'):
        print("event up")
        moveUp(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
        else:
            sys.exit("Player lost")
        swapTexture(matrix)

    if(chr(ch)=='d'):
        print("event right")
        moveRight(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
        else:
            sys.exit("Player lost")
        swapTexture(matrix)


def Insertion(matrix):
    empty = emptyPlaces(matrix)
    random.shuffle(empty)
    numIndex = empty.pop()
    x, y = returnNum(numIndex)
    value1=insertNum(matrix, x, y)
    print(f"Element inserted")
    matrixPrint(matrix)
    return value1 , x, y

def main():
    pygame.init()
    values=Insertion(matrix)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Kursova2048")
    glEnable(GL_TEXTURE_2D)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(Cube)
    glutKeyboardFunc(keybrd)

    glutMainLoop()


main()



##Python 3.7 PyOpenGL 1.11a1 +PyGame

##Sorry that all is in the 1 file, u can split it by yourself

##How to play: press Enter
##WASD- to move up/left/down/right

##100% working logic of the game
##In future: normal tex, menu, messages about end or start

