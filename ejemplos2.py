from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4.4, 4.4, -4.4, 4.4)

def dibujar_texto(x, y, texto, r=1.0, g=1.0, b=1.0):
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)

    # Ejes principales
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-4, 0)
    glVertex2f(4, 0)
    glVertex2f(0, -4)
    glVertex2f(0, 4)
    glEnd()

    # Texto ejes
    dibujar_texto(4.1, -0.2, "X", 1.0, 0.8, 0.2)
    dibujar_texto(-0.2, 4.1, "Y", 1.0, 0.8, 0.2)

    # Marcas y números eje X
    for i in range(-4, 5):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i, -0.08)
            glVertex2f(i,  0.08)
            glEnd()
            dibujar_texto(i - 0.1, -0.3, str(i))

    # Marcas y números eje Y
    for j in range(-4, 5):
        if j != 0:
            glBegin(GL_LINES)
            glVertex2f(-0.08, j)
            glVertex2f( 0.08, j)
            glEnd()
            dibujar_texto(0.2, j - 0.1, str(j))

    # Gráfica y = sin(x)
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-4, 4, 300):
        y = np.sin(x)
        glVertex2f(x, y)
    glEnd()

  

    # Título
    dibujar_texto(-1.2, 4.3, "Grafica de y = x^2", 0.8, 1.0, 0.6)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"PLANO CARTESIANO - y = x^2 (Luz)")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()
