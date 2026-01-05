from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

class TexturedCube:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.textures = []
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        glutCreateWindow(b"Cubo 3D con Texturas")

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        glClearColor(0.2, 0.3, 0.4, 1.0)

        self.load_textures()

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    # ----------------------------
    # Cargar 6 texturas con PIL
    # ----------------------------
    def load_textures(self):
        image_files = [
            "cara1.jpg", "cara2.jpg", "cara3.jpg",
            "cara4.jpg", "cara5.jpg", "cara6.jpg"
        ]

        self.textures = glGenTextures(6)

        for i, img_file in enumerate(image_files):
            img = Image.open(img_file)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img_data = img.convert("RGB").tobytes()

            glBindTexture(GL_TEXTURE_2D, self.textures[i])
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                         img.width, img.height,
                         0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # ----------------------------
    # Dibuja el cubo texturizado SIN errores
    # ----------------------------
    def draw_cube(self):

        # ---- CARA 1 (Frente) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[0])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1,  1)
        glTexCoord2f(1, 0); glVertex3f( 1, -1,  1)
        glTexCoord2f(1, 1); glVertex3f( 1,  1,  1)
        glTexCoord2f(0, 1); glVertex3f(-1,  1,  1)
        glEnd()

        # ---- CARA 2 (Atrás) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[1])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
        glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
        glTexCoord2f(1, 1); glVertex3f( 1,  1, -1)
        glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)
        glEnd()

        # ---- CARA 3 (Izquierda) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[2])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
        glTexCoord2f(1, 0); glVertex3f(-1, -1,  1)
        glTexCoord2f(1, 1); glVertex3f(-1,  1,  1)
        glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)
        glEnd()

        # ---- CARA 4 (Derecha) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(1, -1, -1)
        glTexCoord2f(1, 0); glVertex3f(1, -1,  1)
        glTexCoord2f(1, 1); glVertex3f(1,  1,  1)
        glTexCoord2f(0, 1); glVertex3f(1,  1, -1)
        glEnd()

        # ---- CARA 5 (Arriba) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[4])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, 1,  1)
        glTexCoord2f(1, 0); glVertex3f( 1, 1,  1)
        glTexCoord2f(1, 1); glVertex3f( 1, 1, -1)
        glTexCoord2f(0, 1); glVertex3f(-1, 1, -1)
        glEnd()

        # ---- CARA 6 (Abajo) ----
        glBindTexture(GL_TEXTURE_2D, self.textures[5])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1,  1)
        glTexCoord2f(1, 0); glVertex3f( 1, -1,  1)
        glTexCoord2f(1, 1); glVertex3f( 1, -1, -1)
        glTexCoord2f(0, 1); glVertex3f(-1, -1, -1)
        glEnd()

    # ----------------------------
    # Display
    # ----------------------------
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0, 0, -6)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.draw_cube()

        glutSwapBuffers()

    # ----------------------------
    # Rotación con flechas
    # ----------------------------
    def keyboard(self, key, x, y):
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
    TexturedCube()
