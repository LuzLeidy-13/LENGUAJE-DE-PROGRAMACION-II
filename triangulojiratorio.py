import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angulo = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Coordenadas 2D
    glMatrixMode(GL_MODELVIEW)
    
def display():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar rotación
    glRotatef(angulo, 0.0, 0.0, 1.0)
    
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
    global angulo
    if key == GLUT_KEY_LEFT:  # Flecha izquierda
        angulo -= 5
    elif key == GLUT_KEY_RIGHT:  # Flecha derecha
        angulo += 5
    glutPostRedisplay()

    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotacion de Triangulo")  # <- sin acento, con b
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == '__main__':
    main()
