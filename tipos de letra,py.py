from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-4.4, 4.4, -4.4, 4.4)  # Proyección ortogonal 2D

def dibujar_texto(x, y, texto, r=1.0, g=1.0, b=1.0):
    """Función para escribir texto en pantalla"""
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)

    # Ejes coordenados
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-1.5, 0.0)
    glVertex2f(1.5, 0.0)
    glVertex2f(0.0, -1.5)
    glVertex2f(0.0, 1.5)
    glEnd()

    # Etiquetas de los ejes
    dibujar_texto(1.55, -0.05, "X", 1.0, 0.8, 0.2)
    dibujar_texto(-0.1, 1.6, "Y", 1.0, 0.8, 0.2)

    # Marcas y valores del eje X
    for i in range(-1, 2):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i, -0.03)
            glVertex2f(i, 0.03)
            glEnd()
            dibujar_texto(i - 0.05, -0.12, str(i))

    # Marcas y valores del eje Y
    for j in range(-1, 2):
        if j != 0:
            glBegin(GL_LINES)
            glVertex2f(-0.03, j)
            glVertex2f(0.03, j)
            glEnd()
            dibujar_texto(0.08, j - 0.03, str(j))

    # Dibujar la parábola y = x^2
    glColor3f(0.2, 0.8, 1.0)
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-4.4, 4.4, 200):
        y = x ** 2
        glVertex2f(x, y)
    glEnd()

    # Título o ecuación
    dibujar_texto(-0.3, 1.8, "Grafica de y = x^2", 0.8, 1.0, 0.6)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"COORDENADAS - OpenGL (Leydy)")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()
