from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from logic import *
import pygame

edges = ()  # НЕ ЗАБУТИ!!: ЗЛІВА ВЕРХ НА ПРАВО(ПРОТИ ГОДИН)

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
gameEnd = (
    # 1
    ((-1.0, 1.0),
     (-1.0, -1.0),
     (1.0,-1.0),
     (1.0, 1.0))
)
texture0 = pygame.image.load('textures/0.png')
texture2 = pygame.image.load('textures/2.png')
texture4 = pygame.image.load('textures/4.png')
texture8 = pygame.image.load('textures/8.png')
texture16 = pygame.image.load('textures/16.png')
texture32 = pygame.image.load('textures/32.png')
texture64 = pygame.image.load('textures/64.png')
texture128 = pygame.image.load('textures/128.png')
texture256 = pygame.image.load('textures/256.png')
texture512 = pygame.image.load('textures/512.png')
texture1024 = pygame.image.load('textures/1024.png')
texture2048 = pygame.image.load('textures/2048.png')
texture4096 = pygame.image.load('textures/4096.png')
texture8192 = pygame.image.load('textures/8192.png')
texture16384= pygame.image.load('textures/16384.png')
texture32768 = pygame.image.load('textures/32768.png')
textureEnd = pygame.image.load('textures/GameEnd.png')
textureMenu = pygame.image.load('textures/menu.png')

textures = {
    0: texture0,
    2: texture2,
    4: texture4,
    8: texture8,
    16: texture16,
    32: texture32,
    64: texture64,
    128: texture128,
    256: texture256,
    512: texture512,
    1024: texture1024,
    2048: texture2048,
    4096: texture4096,
    8192: texture8192,
    16384: texture16384,
    32768: texture32768,
}


def swapTexture(matrix):
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            value = matrix[row][clm]
            verticiesId = row * 4 + clm
            subTex(textures[value], verticiesId)


def subTex(textureSurface, verticiesId):
    TextureData = pygame.image.tostring(textureSurface, "RGBA", 1)
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
        glVertex2f(verticies[verticiesId][j][0], verticies[verticiesId][j][1])

    glEnd()
    glFlush()
    return texid



def Cube():
    MenuAndEnd(textureMenu)
    glFlush()


def keybrd(key, x, y):
    ch = ord(key.decode("ascii"))
    print(ch)
    print(chr(233))
    if ch == 13:
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        swapTexture(matrix)
        print("start")

    if((chr(ch)=='r') or (chr(ch)=='к')):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        restart(matrix)
        swapTexture(matrix)

    if (chr(ch) == 'q' or (chr(ch)=='й')):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        sys.exit("exit")

    if (chr(ch) == 'a') or (chr(ch)=='ф'):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        print("event left")
        moveLeft(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
            swapTexture(matrix)
        else:
            MenuAndEnd(textureEnd)

    if (chr(ch) == 's' or (chr(ch)=='ы')):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        print("event down")
        moveDown(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
            swapTexture(matrix)
        else:
            MenuAndEnd(textureEnd)


    if (chr(ch) == 'w' or (chr(ch)=='ц')):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        print("event up")
        moveUp(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
            swapTexture(matrix)
        else:
            MenuAndEnd(textureEnd)


    if (chr(ch) == 'd' or (chr(ch)=='в')):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        print("event right")
        moveRight(matrix)
        if checkNull(matrix) == True:
            Insertion(matrix)
            swapTexture(matrix)
        else:
            MenuAndEnd(textureEnd)


def MenuAndEnd(textureSurface):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0, 0, 0, 1)
    TextureData = pygame.image.tostring(textureSurface, "RGBA", 1)
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
        glVertex2f(gameEnd[j][0], gameEnd[j][1])

    glEnd()
    glFlush()
    return texid



def itemMenu(value):
    if value == 1:
        sys.exit("Exit from menu")
    if value == 2:
        print("Starting form Menu")
        swapTexture(matrix)
    if value==3:
        print("Restart from Menu")
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)
        restart(matrix)
        swapTexture(matrix)
    if value==4:
        print("Left from Menu")
        moveLeft(matrix)
        Insertion(matrix)
        swapTexture(matrix)
    if value==5:
        print("Right from Menu")
        moveRight(matrix)
        Insertion(matrix)
        swapTexture(matrix)
    if value==6:
        print("Up from Menu")
        moveUp(matrix)
        Insertion(matrix)
        swapTexture(matrix)
    if value==7:
        print("Down from Menu")
        moveDown(matrix)
        Insertion(matrix)
        swapTexture(matrix)


def CreateMenu():
    menu = glutCreateMenu(itemMenu)
    glutAddMenuEntry("Exit", 1)
    glutAddMenuEntry("Start", 2)
    glutAddMenuEntry("Restart", 3)
    glutAddMenuEntry("Move Left", 4)
    glutAddMenuEntry("Move Right", 5)
    glutAddMenuEntry("Move Up", 6)
    glutAddMenuEntry("Move Down", 7)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    # Add the following line to fix your code
    return 0
