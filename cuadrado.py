from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Objetos3D:
    def __init__(self):
        self.angle_x = 20
        self.angle_y = 30
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 400)
        glutCreateWindow(b"OpenGL - 3D Cube y Pyramid")

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1.0)

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard_special)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 2.0, 1.0, 50.0)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # --- Vista izquierda: CUBO ---
        glViewport(0, 0, 400, 400)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8.0)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.dibujar_ejes()
        self.dibujar_cubo()

        # --- Vista derecha: PIRÁMIDE ---
        glViewport(400, 0, 400, 400)
        glLoadIdentity()
        glTranslatef(0.0, -1.0, -8.0)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)
        self.dibujar_ejes()
        self.dibujar_piramide()

        glutSwapBuffers()

    def dibujar_ejes(self):
        glBegin(GL_LINES)
        # Eje X (rojo)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(3.0, 0.0, 0.0)
        # Eje Y (verde)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 3.0, 0.0)
        # Eje Z (azul)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 3.0)
        glEnd()

    def dibujar_cubo(self):
        glBegin(GL_QUADS)
        # Frente
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        # Atrás
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)

        # Izquierda
        glColor3f(0, 0, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)

        # Derecha
        glColor3f(1, 1, 0)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)

        # Arriba
        glColor3f(1, 0, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)

        # Abajo
        glColor3f(0, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        glEnd()

    def dibujar_piramide(self):
        glBegin(GL_TRIANGLES)
        # Cara frontal
        glColor3f(1, 0, 0)
        glVertex3f(0, 1.5, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)

        # Cara derecha
        glColor3f(0, 1, 0)
        glVertex3f(0, 1.5, 0)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)

        # Cara trasera
        glColor3f(0, 0, 1)
        glVertex3f(0, 1.5, 0)
        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)

        # Cara izquierda
        glColor3f(1, 1, 0)
        glVertex3f(0, 1.5, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glEnd()

        # Base
        glBegin(GL_QUADS)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)
        glEnd()

    def keyboard_special(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.angle_y += 5
        elif key == GLUT_KEY_LEFT:
            self.angle_y -= 5
        elif key == GLUT_KEY_UP:
            self.angle_x -= 5
        elif key == GLUT_KEY_DOWN:
            self.angle_x += 5
        glutPostRedisplay()

if __name__ == "__main__":
    Objetos3D()
