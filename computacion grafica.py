from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle = 0.0  # Ángulo de rotación

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Fondo negro
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Mover la cámara un poco hacia atrás
    glTranslatef(0.0, 0.0, -6.0)
    
    # Rotar el triángulo
    glRotatef(angle, 1.0, 1.0, 0.0)
    
    # Dibujar un triángulo de colores
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()
    
    glutSwapBuffers()
    angle += 0.5  # Incrementar ángulo para animar

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)  # Aproximadamente 60 FPS

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"PyOpenGL Test - Triangulo 3D")  # ← CORREGIDO
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()


if __name__ == "__main__":
    main()
