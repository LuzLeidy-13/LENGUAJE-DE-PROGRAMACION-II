# -*- coding: utf-8 -*-
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -3.0, 3.0)  # Rango ampliado

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Ejes
    glColor3f(1.0, 1.0, 1.0)  # Blanco
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, -3.0)
    glVertex2f(0.0, 3.0)
    glEnd()

    # Ecuación y = x³
    glColor3f(0.2, 0.8, 1.0)  # Azul celeste
    glBegin(GL_LINE_STRIP)
    
    x_coords = np.linspace(-2.0, 2.0, 400)  # Rango más amplio
    for x in x_coords:
        y = x**2
        glVertex2f(x, y)
        
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Grafica de la Ecuacion y = x^3")
    glutDisplayFunc(dibujar_ecuacion)
    inicializar()
    glutMainLoop()

if __name__ == '__main__':
    main()
