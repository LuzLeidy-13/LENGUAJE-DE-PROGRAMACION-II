from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glColor3f(1.0, 0.5, 0.0)          # Color naranja del zorro
    glLineWidth(2)
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)      # Vista 2D centrada

def dibujar_zorro():
    glClear(GL_COLOR_BUFFER_BIT)

    # Contorno principal
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, 0.6)   # Oreja izquierda
    glVertex2f(-0.3, 0.8)
    glVertex2f(-0.1, 0.6)
    glVertex2f(0.1, 0.6)
    glVertex2f(0.3, 0.8)
    glVertex2f(0.6, 0.6)    # Oreja derecha
    glVertex2f(0.4, 0.3)
    glVertex2f(0.25, 0.0)
    glVertex2f(0.0, -0.4)   # Nariz inferior
    glVertex2f(-0.25, 0.0)
    glVertex2f(-0.4, 0.3)
    glEnd()

    # Nariz
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0.0, -0.4)
    glVertex2f(-0.05, -0.35)
    glVertex2f(0.05, -0.35)
    glEnd()

    # Ojos (pequeños triángulos negros)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.25, 0.25)
    glVertex2f(-0.2, 0.3)
    glVertex2f(-0.15, 0.25)

    glVertex2f(0.25, 0.25)
    glVertex2f(0.2, 0.3)
    glVertex2f(0.15, 0.25)
    glEnd()

    # Líneas internas del hocico
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-0.25, 0.0)
    glVertex2f(0.0, -0.4)
    glVertex2f(0.25, 0.0)
    glVertex2f(0.0, -0.4)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cara del Zorro - OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_zorro)
    glutMainLoop()

if __name__ == "__main__":
    main()
