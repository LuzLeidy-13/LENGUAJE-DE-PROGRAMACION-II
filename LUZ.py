from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_letras():
    """Dibuja la palabra LUZ"""
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)  # Color rojo

    glBegin(GL_LINES)

    glVertex2f(-0.8, 0.3); glVertex2f(-0.8, -0.3)  # Línea vertical
    glVertex2f(-0.8, -0.3); glVertex2f(-0.6, -0.3)  # Línea base

    glVertex2f(-0.15, 0.3); glVertex2f(-0.15, -0.3)  # Lateral izquierdo
    glVertex2f(-0.15, -0.3); glVertex2f(0.15, -0.3)  # Base
    glVertex2f(0.15, -0.3); glVertex2f(0.15, 0.3)    # Lateral derecho

    glVertex2f(0.4, 0.3); glVertex2f(0.7, 0.3)   # Parte superior
    glVertex2f(0.7, 0.3); glVertex2f(0.4, -0.3)  # Diagonal
    glVertex2f(0.4, -0.3); glVertex2f(0.7, -0.3) # Parte inferior

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"LUZ ")
    inicializar()
    glutDisplayFunc(dibujar_letras)
    glutMainLoop()

if __name__ == "__main__":
    main()

