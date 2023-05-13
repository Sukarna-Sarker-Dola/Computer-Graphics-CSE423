from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_TRIANGLE(): #building the roof
    glColor3f(0.0, 0.5, 0.5) #setting the greenish blue color
    glPointSize(5) #setting the pixel size
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 250) #Red A
    glVertex2f(400, 250) #Red B
    glVertex2f(300, 400) #Red C
    glEnd()
def draw_LINES(): #bulding the body of the house
    glColor3f(0.0, 0.5, 0.5) #setting the greenish blue color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(200,100) #blue A
    glVertex2f(400,100) #blue B

    glVertex2f(200,100) #blue A
    glVertex2f(200,250) #blue D

    glVertex2f(400, 100) #blue B
    glVertex2f(400, 250) #blue C

    glVertex2f(200, 250) #blue D
    glVertex2f(400, 250) #blue C
    glEnd()

def draw_TRIANGLEWINDOW(): # building the windows and door
    glColor3f(0.0, 0.5, 0.5) #setting the color
    glPointSize(5) #setting the pixel size

    #building the windows
    glBegin(GL_TRIANGLES)  #building WC part
    glVertex2f(350, 180)
    glVertex2f(388, 180)
    glVertex2f(350, 220)
    glEnd()

    glBegin(GL_TRIANGLES) #building WD part
    glVertex2f(388, 180)
    glVertex2f(388, 220)
    glVertex2f(350, 220)
    glEnd()

    glBegin(GL_TRIANGLES) #building WA part
    glVertex2f(212, 180)
    glVertex2f(250, 180)
    glVertex2f(212, 220)
    glEnd()

    glBegin(GL_TRIANGLES) #building WB part
    glVertex2f(250, 180)
    glVertex2f(250, 220)
    glVertex2f(212, 220)
    glEnd()
    #window complete

    #now building the door
    glBegin(GL_TRIANGLES)  #building TA part
    glVertex2f(280, 100)
    glVertex2f(320, 100)
    glVertex2f(280, 180)
    glEnd()

    glBegin(GL_TRIANGLES)  #building TB part
    glVertex2f(320, 100)
    glVertex2f(320, 180)
    glVertex2f(280, 180)
    glEnd()
    #door complete

def draw_POINTS():
    glColor3f(0.0, 0.0, 0.0) #setting the doorknob color to black
    glPointSize(5) #setting the pixel size
    glBegin(GL_POINTS)
    glVertex2f(310,140)
    glEnd()


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
    draw_TRIANGLE() 
    draw_LINES()
    draw_TRIANGLEWINDOW()
    draw_POINTS()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size has been written here
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name is OpenGL Coding Practice
glutDisplayFunc(showScreen)

glutMainLoop()