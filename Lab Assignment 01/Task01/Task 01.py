from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake MEANS POINT SIZE DEFINE KORCHI
    glBegin(GL_POINTS) #build in function jeta point generation er starting a thake GL_POINTS eta diye bujhbe point generate korte hobe for example GL_LINES diye line generate hobe GL_TRIANGLEs diye triangle generate hobe
    glVertex2f(x,y) #jekhane show korbe pixel cause ekhane point generate korche ei line SO EKHAN THEKE SHOWSCREEN A JABE
    glEnd() #build in function jeta point generation er end a thake

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen(): #string window er shob kichu define kora
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB) red=1.0 means full g=1.0 means full B=0.0 so red and green diye yellow hocche
    #call the draw methods here
    for i in range(50):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        draw_points(x, y)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size has been written here
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name is OpenGL Coding Practice
glutDisplayFunc(showScreen)

glutMainLoop()