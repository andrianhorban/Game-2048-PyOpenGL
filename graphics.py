from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

edges=()  #НЕ ЗАБУТИ!!: ЗЛІВА ВЕРХ НА ПРАВО(ПРОТИ ГОДИН)

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

texture0 = pygame.image.load('textures/0.png')
texture2 = pygame.image.load('textures/2.png')
texture4 = pygame.image.load('textures/4.png')
texture8 = pygame.image.load('textures/8.png')
texture16 = pygame.image.load('textures/16.png')
texture32 = pygame.image.load('textures/32.png')
texture64 = pygame.image.load('textures/64.png')

textures = {
    0: texture0,
    2: texture2,
    4: texture4,
    8: texture8,
    16: texture16,
    32: texture32,
    64: texture64
}
def swapTexture(matrix):
    for row in range(len(matrix)):
        for clm in range(len(matrix)):
            value=matrix[row][clm]
            verticiesId=row*4+clm
            subTex(textures[value],verticiesId)


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

