from graphics import *
import sys

matrixPrint(matrix)


def main():
    pygame.init()
    Insertion(matrix)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Kursova2048")
    glEnable(GL_TEXTURE_2D)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(Cube)
    glutKeyboardFunc(keybrd)
    CreateMenu()

    glutMainLoop()


main()

##Andrian Horban, Lviv National University UKRAINE
##Python 3.7 PyOpenGL 1.11a1 +PyGame

##How to play: press Enter
##WASD - to move up/left/down/right

##100% working logic of the game
##In future: normal tex, menu, messages about end or start
