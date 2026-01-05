import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Variables globales
pos_x = 0.0  # posición horizontal
velocidad = 0.1  # cuánto se mueve en cada tecla

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Coordenadas 2D
    glMatrixMode(GL_MODELVIEW)

def display():
    global pos_x
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar traslación
    glTranslatef(pos_x, 0.0, 0.0)
    
    # Dibujar triángulo con colores RGB
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex2f(0.0, 0.5)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex2f(0.5, -0.5)
    glEnd()
    
    glFlush()

def special_keys(key, x, y):
    global pos_x
    if key == GLUT_KEY_LEFT:   
        pos_x -= velocidad
    elif key == GLUT_KEY_RIGHT:  
        pos_x += velocidad
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Desplazamiento de Triangulo")  # sin acento
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == '__main__':
    main()
