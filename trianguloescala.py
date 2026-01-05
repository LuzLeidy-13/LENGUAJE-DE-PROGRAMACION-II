from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

escala = 1

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0) # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Vista ortográfica 2D

def dibujar_triangulo():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0) # Color amarillo
    glScalef(escala, escala, 1.0)
    glBegin(GL_TRIANGLES)
    #glBegin(GL_POLYGON)
    # Vertice superior
    glVertex2f(-0.5, 0.9) # Vértice inferior izquierdo
    glVertex2f(-0.9, -0.9) # Vértice inferior derecho (x, z)
    glVertex2f(0.5, -0.5)
    glEnd()
    glFlush()

def keyboard(key, x, y):
    global escala
    if key == b'+':
        escala += 0.1
    elif key == b'-':
        escala -= 0.1
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b'Triangulo de puntos en OpenGL')
    inicializar()
    glutDisplayFunc(dibujar_triangulo)
    glutSpecialFunc(keyboard)
    #glutIdleFunc(lambda: glRotatef(angulo, x, y, z))
    glutMainLoop()

if __name__ == '__main__':
    main()
