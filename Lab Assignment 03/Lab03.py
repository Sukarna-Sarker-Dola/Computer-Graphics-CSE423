from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x_prime, y_prime, radius, a, b, c):
    glColor3f(a, b, c)
    glPointSize(5)
    glBegin(GL_POINTS)
    x1 = 0
    y1 = radius
    d = 1 - radius
    while x1 < y1:
        if d < 0:
            d = d + 2 * x1 + 3
            x1 = x1 + 1
            y1 = y1 + 0
            glVertex2f(y1 + x_prime, x1 + y_prime)  # this is zone 0
            glVertex2f(x1 + x_prime, y1 + y_prime) #this is zone 1
            glVertex2f(-x1 + x_prime, y1 + y_prime) #this is zone 2
            glVertex2f(-y1 + x_prime, x1 + y_prime) #this is zone 3
            glVertex2f(-y1 + x_prime, -x1 + y_prime) #this is zone 4
            glVertex2f(-x1 + x_prime, -y1 + y_prime) #this is zone 5
            glVertex2f(x1 + x_prime, -y1 + y_prime) #this is zone 6
            glVertex2f(y1 + x_prime, -x1 + y_prime) #this is zone 7





        elif d >= 0:
            d = d + 2 * x1 - 2 * y1 + 5
            x1 = x1 + 1
            y1 = y1 - 1
            glVertex2f(x1 + x_prime, y1 + y_prime)
            glVertex2f(y1 + x_prime, x1 + y_prime)
            glVertex2f(y1 + x_prime, -x1 + y_prime)
            glVertex2f(x1 + x_prime, -y1 + y_prime)
            glVertex2f(-x1 + x_prime, -y1 + y_prime)
            glVertex2f(-y1 + x_prime, -x1 + y_prime)
            glVertex2f(-y1 + x_prime, x1 + y_prime)
            glVertex2f(-x1 + x_prime, y1 + y_prime)

    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_points(200, 200, 200,0.0, 1.0, 0.0)
    draw_points(300, 200, 100,0.0, 0.0, 1.0)
    draw_points(270, 270, 100,0.5, 1.0, 1.0)
    draw_points(130, 270, 100,1.0, 0.0, 1.0)
    draw_points(270, 130, 100,1.0, 0.5, 0.0)
    draw_points(200, 300, 100,0.5, 0.5, 0.5)
    draw_points(130, 130, 100,0.0, 0.5, 0.5)
    draw_points(100, 200, 100,0.0, 0.5, 1.0)
    draw_points(200, 100, 100,2.0, 0.5, 1.0)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
