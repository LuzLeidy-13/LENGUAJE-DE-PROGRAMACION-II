from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12.0, 12.0, -12.0, 12.0, -1.0, 1.0)  # Vista ortográfica 2D


def dibujar_zorro():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.4, 0.0)
    glBegin(GL_LINES)

    # Parte inferior del zorro (cara)
    glVertex2f(0, 1); glVertex2f(-3, 4)
    glVertex2f(-3, 4); glVertex2f(-7, 1)
    glVertex2f(-7, 1); glVertex2f(-8, -2)
    glVertex2f(-8, -2); glVertex2f(-9, -6)
    glVertex2f(-9, -6); glVertex2f(-8, -7)
    glVertex2f(-8, -7); glVertex2f(-7, -6)
    glVertex2f(-7, -6); glVertex2f(-4, -9)
    glVertex2f(-4, -9); glVertex2f(-1, -10)
    glVertex2f(-1, -10); glVertex2f(1, -10)
    glVertex2f(1, -10); glVertex2f(4, -9)
    glVertex2f(4, -9); glVertex2f(7, -6)
    glVertex2f(7, -6); glVertex2f(8, -7)
    glVertex2f(8, -7); glVertex2f(9, -7)
    glVertex2f(9, -7); glVertex2f(8, -3)
    glVertex2f(8, -3); glVertex2f(7, 1)
    glVertex2f(7, 1); glVertex2f(3, 4)
    glVertex2f(3, 4); glVertex2f(0, 1)

    # Parte superior (frente)
    glVertex2f(-7, 1); glVertex2f(-8, 4)
    glVertex2f(-8, 4); glVertex2f(-9, 7)
    glVertex2f(-9, 7); glVertex2f(-8, 10)
    glVertex2f(-8, 10); glVertex2f(-7, 10)
    glVertex2f(-7, 10); glVertex2f(-5, 9)
    glVertex2f(-5, 9); glVertex2f(-3, 7)
    glVertex2f(-3, 7); glVertex2f(-2, 6)
    glVertex2f(-2, 6); glVertex2f(0, 7)
    glVertex2f(0, 7); glVertex2f(2, 6)
    glVertex2f(2, 6); glVertex2f(3, 7)
    glVertex2f(3, 7); glVertex2f(5, 9)
    glVertex2f(5, 9); glVertex2f(7, 10)
    glVertex2f(7, 10); glVertex2f(8, 10)
    glVertex2f(8, 10); glVertex2f(9, 7)
    glVertex2f(9, 7); glVertex2f(8, 4)
    glVertex2f(8, 4); glVertex2f(7, 1)

    glEnd()

    # OREJAS CON COLOR INTERIOR
    glColor3f(1.0, 0.6, 0.2)
    glBegin(GL_POLYGON)
    glVertex2f(-7, 9); glVertex2f(-7, 4); glVertex2f(-6, 3)
    glVertex2f(-4, 5); glVertex2f(-4, 6); glVertex2f(-5, 7)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(7, 9); glVertex2f(7, 5); glVertex2f(6, 4)
    glVertex2f(4, 5); glVertex2f(4, 6)
    glEnd()

    # Contorno orejas
    glColor3f(1.0, 0.3, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-7, 9); glVertex2f(-7, 4)
    glVertex2f(-7, 4); glVertex2f(-6, 3)
    glVertex2f(-6, 3); glVertex2f(-4, 5)
    glVertex2f(-4, 5); glVertex2f(-4, 6)
    glVertex2f(-4, 6); glVertex2f(-5, 7)
    glVertex2f(-5, 7); glVertex2f(-7, 9)

    glVertex2f(7, 9); glVertex2f(7, 5)
    glVertex2f(7, 5); glVertex2f(6, 4)
    glVertex2f(6, 4); glVertex2f(4, 5)
    glVertex2f(4, 5); glVertex2f(4, 6)
    glVertex2f(4, 6); glVertex2f(7, 9)
    glEnd()

    
    # NARIZ, BOCA Y HOCICO
    glColor3f(0.8, 0.3, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-1, 0); glVertex2f(-2, -4)
    glVertex2f(-2, -4); glVertex2f(-3, -6)
    glVertex2f(-3, -6); glVertex2f(-3, -7)
    glVertex2f(-3, -7); glVertex2f(-1, -8)
    glVertex2f(-1, -8); glVertex2f(1, -8)
    glVertex2f(1, -8); glVertex2f(3, -7)
    glVertex2f(3, -7); glVertex2f(3, -6)
    glVertex2f(3, -6); glVertex2f(2, -4)
    glVertex2f(2, -4); glVertex2f(1, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-5, -3); glVertex2f(-4, -5)
    glVertex2f(-4, -5); glVertex2f(-3, -7)
    glVertex2f(-3, -7); glVertex2f(-1, -8)
    glVertex2f(-1, -8); glVertex2f(1, -8)
    glVertex2f(1, -8); glVertex2f(3, -7)
    glVertex2f(3, -7); glVertex2f(4, -5)
    glVertex2f(4, -5); glVertex2f(5, -3)
    glEnd()

    glColor3f(1.0, 0.5, 0.2)
    glBegin(GL_LINES)
    glVertex2f(-1, -8); glVertex2f(-2, -6)
    glVertex2f(-2, -6); glVertex2f(-1, -5)
    glVertex2f(-1, -5); glVertex2f(1, -5)
    glVertex2f(1, -5); glVertex2f(2, -6)
    glVertex2f(2, -6); glVertex2f(1, -8)
    glEnd()

  
    # OJOS (RELLENADOS)
    glColor3f(1.0, 1.0, 0.2)
    glBegin(GL_POLYGON)
    glVertex2f(-2, -1); glVertex2f(-4, 0); glVertex2f(-5, 0); glVertex2f(-4, -1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4, 0); glVertex2f(5, 0); glVertex2f(4, -1); glVertex2f(2, -1)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Zorro - GL_LINES y Poligonos")
    inicializar()
    glutDisplayFunc(dibujar_zorro)
    glutMainLoop()


if __name__ == "__main__":
    main()
