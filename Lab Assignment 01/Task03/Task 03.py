from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_LINESONE(): #writing 1
    glColor3f(1.0, 0.0, 0.0) #setting the red color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(20,100) #A
    glVertex2f(60,100) #B

    glVertex2f(40,100) #D
    glVertex2f(40,300) #C

    glVertex2f(40,300) #C
    glVertex2f(30,250) #E
    glEnd()

def draw_LINESNINE(): #writing 9
    glColor3f(0.0, 1.0, 0.0) #setting the GREEN color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(70,100) #A
    glVertex2f(110,100) #B

    glVertex2f(110,100) #B
    glVertex2f(110,300) #C

    glVertex2f(110,300) #C
    glVertex2f(70,300) #D

    glVertex2f(70,300) #D
    glVertex2f(70,200) #E

    glVertex2f(70,200) #E
    glVertex2f(110,200) #F
    glEnd()

def draw_LINESTHREE(): #writing 3
    glColor3f(0.0, 0.0, 1.0)  #setting the GREEN color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(120,100) #A
    glVertex2f(160,100) #B

    glVertex2f(160,100) #B
    glVertex2f(160,300) #C

    glVertex2f(160,300) #C
    glVertex2f(120,300) #D

    glVertex2f(120,200) #E
    glVertex2f(160,200) #F
    glEnd()

def draw_LINESZERO(): #writing 0
    glColor3f(0.5, 1.0, 1.0)  #setting the CYAN color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(170,100) #A
    glVertex2f(210,100) #B

    glVertex2f(210,100) #B
    glVertex2f(210,300) #C

    glVertex2f(210,300) #C
    glVertex2f(170,300) #D

    glVertex2f(170,300) #D
    glVertex2f(170,100) #A
    glEnd()

def draw_LINESONEE(): #writing 1
    glColor3f(1.0, 0.0, 1.0) #setting the PURPLE color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(220,100) #A
    glVertex2f(260,100) #B

    glVertex2f(240,100) #D
    glVertex2f(240,300) #C

    glVertex2f(240,300) #C
    glVertex2f(230,250) #E
    glEnd()

def draw_LINESTWO(): #writing 2
    glColor3f(1.0, 0.5, 0.0) #setting the PURPLE color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(270,100) #A
    glVertex2f(310,100) #B

    glVertex2f(270,100) #A
    glVertex2f(270,200) #C

    glVertex2f(270,200) #C
    glVertex2f(310,200) #D

    glVertex2f(310,200) #D
    glVertex2f(310,300) #E

    glVertex2f(270,300) #F
    glVertex2f(310,300) #E
    glEnd()

def draw_LINESZEROO(): #writing 0
    glColor3f(0.5, 0.5, 0.5)  #setting the VIOLET color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(320,100) #A
    glVertex2f(360,100) #B

    glVertex2f(360,100) #B
    glVertex2f(360,300) #C

    glVertex2f(360,300) #C
    glVertex2f(320,300) #D

    glVertex2f(320,300) #D
    glVertex2f(320,100) #A
    glEnd()

def draw_LINESONEEE(): #writing 1
    glColor3f(1.0, 1.0, 0.0) #setting the YELLOW color
    glPointSize(5) # setting the pixel size
    glBegin(GL_LINES)
    glVertex2f(370,100) #A
    glVertex2f(410,100) #B

    glVertex2f(390,100) #D
    glVertex2f(390,300) #C

    glVertex2f(390,300) #C
    glVertex2f(380,250) #E
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
    draw_LINESONE() #1
    draw_LINESNINE() #9
    draw_LINESTHREE() #3
    draw_LINESZERO() #0
    draw_LINESONEE() #1
    draw_LINESTWO() #2
    draw_LINESZEROO() #0
    draw_LINESONEEE() #1

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size has been written here
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name is OpenGL Coding Practice
glutDisplayFunc(showScreen)

glutMainLoop()