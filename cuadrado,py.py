from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    """Configura el entorno OpenGL"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glPointSize(5)                    # Tamaño de los puntos
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)  # Vista ortográfica 2D

def dibujar_cuadrado():
    """Dibuja 4 puntos formando un cuadrado"""
    glClear(GL_COLOR_BUFFER_BIT)  # Borra la pantalla

    glBegin(GL_POINTS)

    # Cuatro vértices del cuadrado
    glColor3f(1.0, 0.0, 0.0); glVertex2f(-0.5, 0.5)   # Superior izquierdo
    glColor3f(0.0, 1.0, 0.0); glVertex2f(0.5, 0.5)    # Superior derecho
    glColor3f(0.0, 0.0, 1.0); glVertex2f(-0.5, -0.5)  # Inferior izquierdo
    glColor3f(1.0, 1.0, 0.0); glVertex2f(0.5, -0.5)  

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cuadrado de puntos en OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_cuadrado)
    glutMainLoop()

if __name__ == "__main__":
    main()
